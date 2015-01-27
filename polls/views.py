from django.http import HttpResponse
from django.template import RequestContext,loader
from polls.models import Question,Choice
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

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
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

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
