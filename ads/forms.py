from ckeditor.widgets import CKEditorWidget
from django import forms

from ads.models import Ad, CategoryCity, Category


class AdForm(forms.ModelForm):
    # description = forms.CharField(widget=CKEditorWidget())
    phone_number = forms.IntegerField(
        min_value=100000000, max_value=999999999,
        error_messages={
            'required': "Bu maydonni to'ldirish talab qilinadi",
            "invalid": "Iltiomos to'g'ri qiymat kiriting!",
            'max_value': "Raqam 9tadan ko'p yoki kam bo'lmasligi kerak",
            'min_value': "Raqam 9tadan ko'p yoki kam bo'lmasligi kerak",
        },

    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        error_messages={
            'required': 'Kategoriyani tanlang'
        }
    )
    category_city = forms.ModelChoiceField(
        queryset=CategoryCity.objects.all(),
        error_messages={
            'required': 'Joylashuvni tanlang'
        }
    )
    price = forms.IntegerField(
        min_value=0,
        max_value=999999999999,
        error_messages={
            'required': "Bu maydonni to'ldirish talab qilinadi",
            'invalid': "Iltimos to'g'ri qiymat kiriting",
            'max_value': 'Bu qiymat 999999999999 dan kichik yoki unga teng ekanligiga ishonch hosil qiling.'
        }
    )

    class Meta:
        model = Ad
        fields = (
            'title', 'category', 'price', 'currency', 'category_city',
            'description', 'image', 'image2', 'image3', 'image4', 'phone_number',
        )
