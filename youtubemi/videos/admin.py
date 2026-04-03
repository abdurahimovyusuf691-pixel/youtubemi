from django.contrib import admin
from .models import Video

admin.site.register(Video)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

admin.site.register(CustomUser, UserAdmin)
