from ads.models import Ad, Category, CategoryCity


def global_context(request):
    all_category = Category.objects.all()
    global_ad_count = Ad.objects.count()
    global_category_city = CategoryCity.objects.all()

    context = {
        'global_all_category': all_category,
        'global_category_city': global_category_city,
        'global_ad_count': global_ad_count,


    }
    return context
