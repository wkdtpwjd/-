from django.contrib import admin
# 관리자 계정에서 추가할 필드를 선언

from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(User,UserAdmin)
