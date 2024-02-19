from django import forms


COUNTRIES = [
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

CATEGORIES = [
    ("general", "General"),
    ("business", "Business"),
    ("entertainment", "Entertainment"),
    ("health", "Health"),
    ("science", "Science"),
    ("sports", "Sports"),
    ("technology", "Technology"),
]

LANGUAGES = [
    ("ar", "Arabic"),
    ("de", "German"),
    ("en", "English"),
    ("es", "Spanish"),
    ("fr", "French"),
    ("he", "Hebrew"),
    ("it", "Italian"),
    ("nl", "Dutch"),
    ("no", "Norwegian"),
    ("pt", "Portuguese"),
    ("ru", "Russian"),
    ("sv", "Swedish"),
    ("zh", "Chinese"),
]


class ReadForm(forms.Form):
    country = forms.ChoiceField(choices=COUNTRIES)
    category = forms.ChoiceField(choices=CATEGORIES)

    def clean_field(self, field_name):
        return self.cleaned_data[field_name]


class SearchForm(forms.Form):
    search = forms.CharField(max_length=500)
    domains = forms.CharField(max_length=50, required=False)
    exclude_domains = forms.CharField(max_length=50, required=False)
    date_from = forms.DateField(required=False)
    date_to = forms.DateField(required=False)
    language = forms.ChoiceField(
        required=False, choices=LANGUAGES, initial=("en", "English")
    )

    def clean_field(self, field_name):
        return self.cleaned_data[field_name]
