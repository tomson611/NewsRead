def date_to_iso(form, field):
    value = (
        form.cleaned_data[field].isoformat()
        if form.cleaned_data[field] is not None
        else ""
    )
    return value
