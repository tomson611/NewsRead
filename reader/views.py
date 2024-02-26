from datetime import datetime

import requests
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

from newsread.local_settings import API_KEY
from reader.forms import ReadForm, SearchForm, SourcesForm
from reader.functions import date_to_iso


def read_view(request):
    if request.method == "POST":
        form = ReadForm(request.POST)
        if form.is_valid():
            country = form.cleaned_data["country"]
            category = form.cleaned_data["category"]

            try:
                url = (
                    f"https://newsapi.org/v2/top-headlines?"
                    f"country={country}"
                    f"&category={category}"
                    f"&pagesize=100"
                    f"&apiKey={API_KEY}"
                )
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

            return HttpResponseRedirect("read?page=1")

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
            domains = form.cleaned_data["domains"]
            exclude_domains = form.cleaned_data["exclude_domains"]
            date_to = date_to_iso(form, "date_to")
            date_from = date_to_iso(form, "date_from")
            language = form.cleaned_data["language"]
            sort_by = form.cleaned_data["sort_by"]

            try:
                url = (
                    f"https://newsapi.org/v2/everything?"
                    f"q={search}"
                    f"&domains={domains}"
                    f"&excludeDomains={exclude_domains}"
                    f"&language={language}"
                    f"&from={date_from}"
                    f"&to={date_to}"
                    f"&sortBy={sort_by}"
                    f"&apiKey={API_KEY}"
                )

                response = requests.get(url)
                response.raise_for_status()

                data = response.json()

                search_data = data.get("articles", [])

                for item in search_data:
                    date_time = datetime.fromisoformat(item["publishedAt"])
                    date_time_str = date_time.strftime("%m-%d-%Y")
                    item["publishedAt"] = date_time_str

                request.session["search_data"] = search_data
                request.session["search"] = search
                request.session["domains"] = domains
                request.session["exclude_domains"] = exclude_domains
                request.session["date_to"] = date_to
                request.session["date_from"] = date_from
                request.session["language"] = language
                request.session["sort_by"] = sort_by

            except requests.RequestException as e:
                messages.error(request, f"Error making API request: {e}")
                return HttpResponseRedirect("search")

            except ValueError as e:
                messages.error(request, f"Error parsing JSON response: {e}")
                return HttpResponseRedirect("search")

            return HttpResponseRedirect("search?page=1")

        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect("search")

    else:
        form = SearchForm(
            initial={
                "search": request.session.get("search"),
                "domains": request.session.get("domains"),
                "exclude_domains": request.session.get("exclude_domains"),
                "date_to": request.session.get("date_to"),
                "date_from": request.session.get("date_from"),
                "language": request.session.get("language", "en"),
                "sort_by": request.session.get("sort_by"),
            }
        )

    paginator = Paginator(request.session.get("search_data", []), 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"form": form, "page_obj": page_obj}

    return render(request, "reader/search.html", context)


def sources_view(request):
    if request.method == "POST":
        form = SourcesForm(request.POST)
        if form.is_valid():
            country = form.cleaned_data["country"]
            category = form.cleaned_data["category"]
            language = form.cleaned_data["language"]

            try:
                url = (
                    f"https://newsapi.org/v2/top-headlines/sources?"
                    f"&language={language}"
                    f"&category={category}"
                    f"&country={country}"
                    f"&apiKey={API_KEY}"
                )

                response = requests.get(url)
                response.raise_for_status()

                data = response.json()

                sources_data = data.get("sources", [])
                print(sources_data)

                request.session["sources_data"] = sources_data
                request.session["language"] = language
                request.session["country"] = country
                request.session["category"] = category

            except requests.RequestException as e:
                messages.error(request, f"Error making API request: {e}")
                return HttpResponseRedirect("search")

            except ValueError as e:
                messages.error(request, f"Error parsing JSON response: {e}")
                return HttpResponseRedirect("search")

            return HttpResponseRedirect("sources?page=1")

        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect("sources")

    else:
        form = SourcesForm(
            initial={
                "language": request.session.get("language", "en"),
                "country": request.session.get("country", "us"),
                "category": request.session.get("category", "business"),
            }
        )

    paginator = Paginator(request.session.get("sources_data", []), 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"form": form, "page_obj": page_obj}

    return render(request, "reader/sources.html", context)


def home_view(request):
    return render(request, "reader/base.html")
