from django.contrib import admin

from blog_api.user.models import CustomUser
# Register your models here.

admin.site.register(CustomUser)