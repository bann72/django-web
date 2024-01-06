from django import forms
from .models import MainOrderInfo
from django.forms import modelformset_factory


class MainOrderInfoForm(forms.ModelForm):
    class Meta:
        model = MainOrderInfo
        fields = ["znum", "prod", "count", "client", "invorder", "lastday", "file"]


class OrderForm(forms.ModelForm):
    class Meta:
        model = MainOrderInfo
        fields = ["znum", "prod", "count", "client", "invorder", "lastday", "file"]
        widgets = {
            "lastday": forms.DateInput(attrs={"type": "date"}),
        }
