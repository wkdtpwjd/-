from django.contrib import admin
from .models import Article

# Register your models here.
# 관리자 페이지에서 Article 등록하기
admin.site.register(Article)