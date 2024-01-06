from django import forms


class DoPT(forms.Form):
    rdy = forms.IntegerField(label="Вырезано")
