from django.contrib import admin
from .models import Article


# admin 사이트에 등록하겠다.
admin.site.register(Article)