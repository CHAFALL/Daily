from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
# 하나 더 붙어있네??(TEST)
admin.site.register(User, UserAdmin)
