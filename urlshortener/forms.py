from django import forms

from .models import Shortener


class ShortenerForm(forms.ModelForm):
    user_url = forms.URLField(widget=forms.URLInput(
        attrs={"placeholder": "Your URL to shorten"}))

    class Meta:
        model = Shortener

        fields = ('user_url',)
