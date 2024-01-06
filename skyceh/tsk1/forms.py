from django import forms
from .models import Task


class PlasmaTaskForm(forms.ModelForm):
    MANS = (
        (None, "Выберите ответственного"),
        ("оператор чпу", "оператор чпу"),
    )
    man = forms.ChoiceField(choices=MANS, label="Ответственный")
    spot = forms.CharField(
        initial="плазма",  # Устанавливаем значение по умолчанию
        widget=forms.HiddenInput(),  # Скрываем виджет
        required=False,  # делаем его необязательным
    )

    class Meta:
        model = Task
        fields = ("task", "file", "image", "total", "spot", "man", "deadline")
        widgets = {
            "deadline": forms.DateInput(attrs={"type": "date"}),
        }
