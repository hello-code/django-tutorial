# coding: utf-8

from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from polls.models import Question

class QuestionMethondTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        ''' 若日期在将来则不属于最近，返回False '''
        time=timezone.now()+datetime.timedelta(days=30)
        future_question=Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(),False)

    def test_was_published_recently_with_old_question(self):
        '''若日期比昨天还早的不属于最近，返回False'''
        time=timezone.now()-datetime.timedelta(days=30)
        old_question=Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(),False)

    def test_was_published_recently_with_recent_question(self):
        '''若日期在昨天到今天之内的都属于最近。返回True'''
        time=timezone.now()-datetime.timedelta(hours=1)
        recent_question=Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(),True)
