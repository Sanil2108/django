from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from .models import Question, Choice

# Create your views here.
def index(request):
	latest_questions_list = Question.objects.all()
	context = {'latest':latest_questions_list}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	question = Question.objects.all()[question_id - 1]
	choices = question.choice_set.all()
	context = {'choices':choices, 'question':question}
	return render(request, 'polls/detail.html', context)

def results(request, question_id):
	return HttpResponse("You are looking at the results of %s. " % question_id)

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk = request.POST['choice'])

		selected_choice.votes += 1
		selected_choice.save()
	except (KeyError, Choice.DoesNotExist):
		return HttpResponse("Not working")
		pass
	return HttpResponse("You are voting on question %s. " % question_id)