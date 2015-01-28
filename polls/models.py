# coding: utf-8

from django.db import models

# Create your models here.
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    test=models.CharField(max_length=2)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now=timezone.now()
        # 天数-几天才算“最近”
        days=datetime.timedelta(days=1) # 1天=昨天
        return now-days<=self.pub_date<=now
        #return self.pub_date<=now>=now-days 这句语法不对！？测试不通过。

    was_published_recently.admin_order_field='pub_date'
    was_published_recently.boolean=True
    was_published_recently.short_description='Recent Publised'

class Choice(models.Model):
    question=models.ForeignKey(Question)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
