from ads.models import Ad, Category


def global_context(request):
    all_category = Category.objects.all()
    global_ad_count = Ad.objects.count()

    context = {
        'global_all_category': all_category,
        'global_ad_count': global_ad_count,


    }
    return context
