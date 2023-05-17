from django import forms

from ads.models import Ad


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = (
            'title', 'category', 'price', 'currency', 'category_city',
            'description', 'image', 'image2', 'image3', 'image4', 'phone_number'
        )
