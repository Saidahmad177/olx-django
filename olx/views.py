from django.shortcuts import render
from django.views import View

from ads.models import Category, Ad


class HomePageView(View):
    def get(self, request):
        ads = Ad.objects.all()
        all_category = Category.objects.all()

        context = {
            'ads': ads,
            'all_category': all_category,
            'elon': 110909,
        }
        return render(request, 'home.html', context)
