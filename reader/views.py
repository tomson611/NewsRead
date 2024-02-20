from datetime import datetime

import requests
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

from newsread.local_settings import API_KEY
from reader.forms import ReadForm, SearchForm
from reader.functions import date_to_iso


def read_view(request):
    if request.method == "POST":
        form = ReadForm(request.POST)
        if form.is_valid():
            country = form.cleaned_data["country"]
            category = form.cleaned_data["category"]

            try:
                url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&pagesize=100&apiKey={API_KEY}"
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                api_data = data.get("articles", [])

                request.session["api_data"] = api_data
                request.session["country"] = country
                request.session["category"] = category

            except requests.RequestException as e:
                messages.error(request, f"Error making API request: {e}")
                return HttpResponseRedirect("read")

            except ValueError as e:
                messages.error(request, f"Error parsing JSON response: {e}")
                return HttpResponseRedirect("read")


            url = reverse('read_view', kwargs={'page': 1})
            return HttpResponseRedirect(url)
            # return HttpResponseRedirect("read?page=1")

        else:
            messages.error(request, "Invalid form data")
            return HttpResponseRedirect("read")

    else:
        form = ReadForm(
            initial={
                "country": request.session.get("country", "us"),
                "category": request.session.get("category", "business"),
            }
        )

    paginator = Paginator(request.session.get("api_data", []), 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"form": form, "page_obj": page_obj}

    return render(request, "reader/read.html", context)

def search_view(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search"]
            domains = form.cleaned_data['domains']
            exclude_domains = form.cleaned_data['exclude_domains']

            try:
                url = f"https://newsapi.org/v2/everything?q={search}&domains={domains}&excludeDomains={exclude_domains}&language=en&apiKey={API_KEY}"
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                search_data = data.get("articles", [])

                request.session["search_data"] = search_data
                request.session["search"] = search
                request.session["domains"] = domains
                request.session["exclude_domains"] = exclude_domains
                
            except requests.RequestException as e:
                messages.error(request, f"Error making API request: {e}")
                return HttpResponseRedirect("search")

            except ValueError as e:
                messages.error(request, f"Error parsing JSON response: {e}")
                return HttpResponseRedirect("search")
            
            
            return HttpResponseRedirect("search?page=1")

        else:
            messages.error(request, "Invalid form data")
            return HttpResponseRedirect("search")

    else:
        form = SearchForm(initial={
                "search": request.session.get("search"),
                "domains": request.session.get("domains"),
                "exclude_domains": request.session.get("exclude_domains"),
                
            })

    paginator = Paginator(request.session.get("search_data", []), 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"form": form, "page_obj": page_obj}

    return render(request, "reader/search.html", context)