#coding=utf-8
from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    # 设置显示的内容
    list_display = ('title','slug','pub_date')
admin.site.register(Post,PostAdmin)
