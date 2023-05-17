from django.shortcuts import render
from django.views import View

from ads.models import Category, Ad, CategoryCity


class HomePageView(View):
    def get(self, request):
        ads = Ad.objects.all().order_by('-id')
        all_category = Category.objects.all()

        context = {
            'ads': ads,
            'all_category': all_category,
            'elon': 110909,
        }
        return render(request, 'home.html', context)
