from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from ads.forms import AdForm
from ads.models import Category, CategoryCity


class CreateAd(View):
    def get(self, request):
        all_category = Category.objects.all()
        citys = CategoryCity.objects.all()
        context = {
            'all_category': all_category,
            'citys': citys,
        }

        return render(request, 'ads/CRUD/create_ad.html', context)

    def post(self, request):
        forms = AdForm(request.POST)
        price = request.POST.get('category')
        print(price, '---------=========')
        if forms.is_valid():
            forms.save()
            messages.success(
                request,
                "E'loningiz muvofaqqiyatli joylashtirildi.")
            return redirect('home')

        else:
            print(forms.errors)
            return redirect('ads:create')
