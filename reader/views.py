from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib import messages
from newsread.local_settings import API_KEY
from reader.forms import ReadForm
import requests


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

    return render(request, "reader/reader.html", context)
