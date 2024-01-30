from django import forms
from crud.models import ClassRoom


class ClassRoomModelForm(forms.ModelForm):
    class Meta:
        fields = ["name", ]
        model = ClassRoom
