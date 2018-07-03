from django.http import Http404
from django.shortcuts import render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404("不存在！")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "结果 %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("投票 %s" % question_id)
