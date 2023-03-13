from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddArticleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Выбрать'

    class Meta:
        model = Article
        fields = ['title', 'slug', 'annotation', 'content', 'image', 'is_published', 'category']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):  # Функция должна начинаться на 'clean_' + поле для валидации
        title = self.cleaned_data['title']
        if len(title) > 100:
            raise ValidationError('Длина превышает 100 символов')
        return title

