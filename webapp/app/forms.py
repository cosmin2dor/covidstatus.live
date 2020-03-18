from django import forms


class SubscribeForm(forms.Form):
    email = forms.EmailField(label="email", max_length=100)
    country_name = forms.CharField(label="country_name", max_length=100)