from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin

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
            print(form.errors)
            form = AdForm(request.POST)
            select_value = request.POST.get('category')
            # print(form.category)
            print(select_value, 'ssssssssssssssssss')
            # print(form.phone_number)
            # messages.info(request, "Barcha qiymatlarni to'g'ri kiritganingizga ishonch hosil qiling", extra_tags='danger')

            return render(request, 'ads/CRUD/create_ad.html', {'form': form, 'select_val': select_value})


class DetailAdView(View):
    def get(self, request, category, slug):
        item = Ad.objects.get(slug=slug)
        category = Category.objects.get(slug=category)

        context = {}
        # hitcount logic
        hit_count = get_hitcount_model().objects.get_for_object(item)
        hits = hit_count.hits
        hitcontext = context['hitcount'] = {'pk': hit_count.pk}
        hit_count_response = HitCountMixin.hit_count(request, hit_count)
        if hit_count_response.hit_counted:
            hits = hits + 1
            hitcontext['hit_counted'] = hit_count_response.hit_counted
            hitcontext['hit_message'] = hit_count_response.hit_message
            hitcontext['total_hits'] = hits

        context = {
            'detail': item,
            'category': category,
        }
        return render(request, 'ads/detail.html', context)


class CategoryItems(View):
    def get(self, request, category):
        selected_category = Category.objects.get(slug=category)
        category_items = Ad.objects.filter(category=selected_category.id)

        context = {
            'category_items': category_items,
            'selected_category': selected_category,
        }
        return render(request, 'ads/category_items.html', context)

