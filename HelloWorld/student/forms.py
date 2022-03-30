# coding:utf-8
from __future__ import unicode_literals

from django import forms

from .models import Student

class StudentForm(forms.ModelForm):
    #修改对应字段类型，增加QQ号必须为纯数字的校验
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字！')

        return int(cleaned_data)

    def clean_phone(self):
        cleaned_data = self.cleaned_data['phone']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字！')

        return int(cleaned_data)

    #通过复用model来定义form
    class Meta:
        model = Student
        fields = (
            'name', 'sex', 'profession',
            'email', 'qq', 'phone'
        )