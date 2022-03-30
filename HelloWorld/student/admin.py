# -*- coding: utf-8 -*-
# Register your models here.

from __future__ import unicode_literals
from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    #添加信息时需要填入的内容
    list_display = ('id', 'name', 'sex', 'profession', 'email', 'qq', 'phone', 'status', 'created_time')
    #侧边栏显示的过滤器
    list_filter = ('sex', 'status', 'created_time')
    #筛选范围
    search_fields = ('name', 'profession')
    #添加信息界面显示的布局
    fieldsets = (
        (None, {
         'fields': (
                 'name',
                 ('sex', 'profession'),
                 ('email', 'qq', 'phone'),
                 'status',
                 )
         }),
    )

#student注册admin界面
admin.site.register(Student, StudentAdmin)