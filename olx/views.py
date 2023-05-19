from django.db.models import Q
from django.shortcuts import render
from django.views import View

from ads.models import Category, Ad, CategoryCity


class HomePageView(View):
    def get(self, request):
        ads = Ad.objects.all().order_by('-id')
        all_category = Category.objects.all()

        context = {
            'ads': ads[:20],
            'all_category': all_category,
            'elon': ads.count(),
        }
        return render(request, 'home.html', context)


class SearchPageView(View):
    def get(self, request):
        all_ads = Ad.objects.all()
        search = request.GET.get('q', '')
        search_results = 0

        if search:
            search_results = all_ads.filter(Q(title__icontains=search) |
                                            Q(price__icontains=search) |
                                            Q(description__icontains=search) |
                                            Q(category_city__name__icontains=search) |
                                            Q(currency__icontains=search)
                                            )

        context = {
            'search_results': search_results,
            'search_result_count': search_results.count(),
        }
        return render(request, 'search.html', context)
