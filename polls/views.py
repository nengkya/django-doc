from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Question, Choice

# Create your views here.
def venv(request):
    return HttpResponse("<a href>https://www.server-world.info/en/note?os=Debian_12&p=python&f=2</a>")

def index_list(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:4] 
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def index_loader_get_template(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:4]
    template = loader.get_template('polls/index.html') 
    context = {'latest_question_list':latest_question_list}
    return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:6]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)

def detail_hard_coded(request, question_id):
    response = 'You are looking at the question %s'
    return HttpResponse(response % question_id)

def detail_http404(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404('Question on HaGa JanjiNur@gmail.com 20 Nov 2023 doesnt exist !')
    return render(request, 'polls/detail.html', {'question' : question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = 'You are looking at the result of question %s'
    return HttpResponse(response % question_id)

def vote_hard_coded(request, question_id):
    return HttpResponse('You are voting on question %s.' % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
            {'question' : question, 'error_message' : 'You didnt select a choice !'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:vote', args = (question.id, )))













