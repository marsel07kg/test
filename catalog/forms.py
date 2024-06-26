from django import forms
from . import models


class RewiewsForm(forms.ModelForm):
    class Meta:
        model = models.Rewiews
        fields = "__all__"