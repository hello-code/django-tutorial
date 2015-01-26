from django.http import HttpResponse
from django.template import RequestContext,loader
from polls.models import Question
from django.shortcuts import render,get_object_or_404
from django.http import Http404

def index(request):
    # qlist=Question.objects.all()
    # #qlist=Question.objects.order_by('-pub_date')[:5]
    # #output=','.join([p.question_text for p in qlist])
    # # use tmplate
    # template=loader.get_template('polls/index.html')
    # context=RequestContext(request,{'qlist':qlist})
    # return HttpResponse(template.render(context))
    # #return HttpResponse('hello...:'+output)

    qlist=Question.objects.all()
    context={'qlist':qlist}
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    # try:
    #     q=Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('question_id does not exist')
    # return render(request,'polls/detail.html',{'question':q})

    q=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':q})

def results(request,question_id):
    return HttpResponse('results is %s,'%question_id)

def vote(request,question_id):
    return HttpResponse('voting on question %s.'%question_id)
