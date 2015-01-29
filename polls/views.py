# coding: utf-8

from polls.models import Question,Choice
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    '''template_name:视图模板名称;
    context_object_name：准备要显示的数据;
    get_queryset：给上下文(context_object_name)提供数据
    这些都是django内置的'''

    template_name='polls/index.html'
    context_object_name='qlist'

    def get_queryset(self):
        '''Rerurn the last five published questions.
        不包含时间在未来的'''
        #return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    '''显示明细 model也是django内置的属性-模型'''
    model=Question
    template_name='polls/detail.html'

    def get_queryset(self):
        '''Excludes any questions than are not published yet'''
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model=Question
    template_name='polls/results.html'

# def index(request):
#     qlist=Question.objects.all()
#     context={'qlist':qlist}
#     return render(request,'polls/index.html',context)

# def detail(request,question_id):
#     q=get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/detail.html',{'question':q})

# def results(request,question_id):
#     question=get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/results.html',{'question':question})

def vote(request,question_id):
    p=get_object_or_404(Question,pk=question_id)
    try:
        selected=p.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':p,
            'error_message':'pleasssse select'
        })
    else:
        selected.votes+=1
        selected.save()
    return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))
