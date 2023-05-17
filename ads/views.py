from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from ads.forms import AdForm
from ads.models import Category, CategoryCity, Ad


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
        form = AdForm(data=request.POST, files=request.FILES)
        price = request.POST.get('category')
        print(price, '---------=========')
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "E'loningiz muvofaqqiyatli joylashtirildi.")
            return redirect('home')

        else:
            messages.info(request, "Barcha qiymatlarni to'g'ri kiritganingizga ishonch hosil qiling", extra_tags='danger')
            return redirect('ads:create')


class DetailAdView(View):
    def get(self, request, category, slug):
        item = Ad.objects.get(slug=slug)
        category = Category.objects.get(slug=category)

        context = {
            'detail': item,
            'category': category,
        }
        return render(request, 'ads/detail.html', context)
