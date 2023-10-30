from django import forms
from .models import UrlMap

class UrlForm(forms.ModelForm):

    class Meta:
        model = UrlMap
        exclude = ("short_url", )