# coding: utf-8

from django.contrib import admin

# Register your models here.
from polls.models import Question,Choice

#class ChoiceInline(admin.StackedInline): # 把model作为内联嵌入
class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=2 # 显示几项

# 字段顺序(还可以折叠)
class QuestionAdmin(admin.ModelAdmin):
    #fields=['pub_date','question_text']
    fieldsets=[
        ('问题',{'fields':['question_text']}),
        ('日期',{'fields':['pub_date'],'classes':['collapse']}),
        ('测试',{'fields':['test']})
    ]
    inlines=[ChoiceInline]
    list_display=('question_text','pub_date','was_published_recently','test')
    list_filter=['pub_date','question_text']
    search_fields=['question_text','test'] # 哪些字段会被查询

admin.site.register(Question,QuestionAdmin)
