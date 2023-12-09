from .models import Category
from django.forms import ModelForm, TextInput, ImageField


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image']

        widgets = {
            "name": TextInput(attrs={
                "class": 'form-control',
                'placeholder': 'Название категории'
            }),
            'image': ImageField(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Изображение категории'
                }
            )

        }
