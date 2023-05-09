from django.contrib import admin

from ads.models import Category, CategoryCity, Ad, Currency

admin.site.register(Category)
admin.site.register(CategoryCity)
admin.site.register(Ad)
admin.site.register(Currency)
