from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
from .form import QuestionPost


# Create your views here.
def question_list(request):
    questions = Question.objects
    return render(request, 'question_list.html', {'question':questions})

def question_detail(request, question_id):
    detail = get_object_or_404(Question, pk=question_id)
    return render(request, 'question_detail.html', {'detail':detail})

def question_post(request):
    if request.method == 'POST':
        form = QuestionPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('question_list')

    else:
        form = QuestionPost()
        return render(request, 'question_post.html', {'form':form})

def question_delete(request, question_id):
    post = get_object_or_404(Question, pk=question_id)

    if request.POST['password'] == post.password:
        post.delete()
        return redirect('question_list')