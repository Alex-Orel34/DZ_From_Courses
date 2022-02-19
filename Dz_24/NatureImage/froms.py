from .models import NatureImage
from django.forms import ModelForm


class NatureImageForm(ModelForm):
    class Meta:
        model = NatureImage
        fields = ['id', 'url', 'width', 'height', 'desc']
