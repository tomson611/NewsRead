from django import forms

country_list = [
    ("ae", "United Arab Emirates"),
    ("ar", "Argentina"),
    ("at", "Austria"),
    ("au", "Australia"),
    ("be", "Belgium"),
    ("bg", "Bulgaria"),
    ("br", "Brazil"),
    ("ca", "Canada"),
    ("ch", "Switzerland"),
    ("cn", "China"),
    ("co", "Colombia"),
    ("cu", "Cuba"),
    ("cz", "Czechia"),
    ("de", "Germany"),
    ("eg", "Egypt"),
    ("fr", "France"),
    ("gb", "Great Britain"),
    ("gr", "Greece"),
    ("hk", "Hong Kong"),
    ("hu", "Hungary"),
    ("id", "Indonesia"),
    ("ie", "Ireland"),
    ("il", "Israel"),
    ("in", "India"),
    ("it", "Italy"),
    ("jp", "Japan"),
    ("kr", "Korea"),
    ("lt", "Lithuania"),
    ("lv", "Latvia"),
    ("ma", "Morocco"),
    ("mx", "Mexico"),
    ("my", "Malaysia"),
    ("ng", "Nigeria"),
    ("nl", "Netherlands"),
    ("no", "Norway"),
    ("nz", "New Zealand"),
    ("ph", "Philippines"),
    ("pl", "Poland"),
    ("pt", "Portugal"),
    ("ro", "Romania"),
    ("rs", "Serbia"),
    ("ru", "Russia"),
    ("sa", "Saudi Arabia"),
    ("se", "Sweden"),
    ("sg", "Singapore"),
    ("si", "Slovenia"),
    ("sk", "Slovakia"),
    ("th", "Thailand"),
    ("tr", "Turkey"),
    ("tw", "Taiwan"),
    ("ua", "Ukraine"),
    ("us", "United States"),
    ("ve", "Venezuela"),
    ("za", "South Africa"),
]

category_list = [
    ("general", "General"),
    ("business", "Business"),
    ("entertainment", "Entertainment"),
    ("health", "Health"),
    ("science", "Science"),
    ("sports", "Sports"),
    ("technology", "Technology"),
]


class ReadForm(forms.Form):
    country = forms.ChoiceField(
        choices=country_list,
    )

    category = forms.ChoiceField(choices=category_list)

    def clean_country(self):
        data = self.cleaned_data["country"]
        return data

    def clean_category(self):
        data = self.cleaned_data["category"]
        return data
    
class SearchForm(forms.Form):
    search = forms.CharField(max_length=500)
    domains = forms.CharField(max_length=50,required=False)
    exclude_domains = forms.CharField(max_length=50,required=False)


    def clean_search(self):
        data = self.cleaned_data['search']
        return data
    
    def clean_domains(self):
        data = self.cleaned_data['domains']
        return data
    
    def clean_exclude_domains(self):
        data = self.cleaned_data['exclude_domains']
        return data