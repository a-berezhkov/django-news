from .models import News
from django.forms import ModelForm, Textarea, TextInput, DateInput, Select


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'body', 'desc', 'date', 'user', 'category']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Название статьи"
            }),
            "desc": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Описание статьи"
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'type': "date"
            }),
            "body": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Текст статьи"
            }),
            "user": Select(attrs={
                'class': 'form-control',
            }),
            "category": Select(attrs={
                'class': 'form-control',
            }),
        }
