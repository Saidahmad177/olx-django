from django.contrib import admin
from users.models import CustomUser, Contact

admin.site.register(CustomUser)
admin.site.register(Contact)
