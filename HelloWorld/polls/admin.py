from django.contrib import admin
from .models import Question,Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    #字段名称的元组，要在对象的更改列表页面上显示为列
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    #Django根据字段类型pub_date，给出合适的过滤选项
    list_filter = ['pub_date']

    #在列表的顶部添加一个搜索框
    search_fields = ['question_text']

#告诉管理，问题 Question 对象需要一个后台接口
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)