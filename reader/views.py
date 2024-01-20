from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View

import requests

from newsread.local_settings import API_KEY
from reader.forms import ReadForm


def read_view(request):
    if request.method == "POST":
        # Create a form instance and populate it with data from the request (binding):
        form = ReadForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            # book_instance.due_back = form.cleaned_data['renewal_date']
            # book_instance.save()
            country = form.cleaned_data["country"]
            category = form.cleaned_data["category"]

            url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={API_KEY}"
            response = requests.get(url)
            data = response.json()
            api_data = data["articles"]
            print(api_data)
            request.session["api_data"] = api_data
            request.session["country"] = country
            request.session["category"] = category
            # return render(request, 'reader/reader.html', {'api_data': api_data})

            # redirect to a new URL:
            # return HttpResponseRedirect('/', {'api_data': api_data})
            # return render(request, 'reader/reader.html', {'api_data': api_data, 'form': form,})
            return HttpResponseRedirect("/")
    # If this is a GET (or any other method) create the default form.
    else:
        form = ReadForm(
            initial={
                "country": request.session.get("country", "us"),
                "category": request.session.get("category", "business"),
            }
        )

    context = {
        "form": form,
    }

    return render(request, "reader/reader.html", context)
