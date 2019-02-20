from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Comment
from .form import QuestionPost, CommentForm


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
            return redirect('question_post')
    else:
        form = QuestionPost()
        return render(request, 'question_post.html', {'form':form})

def question_delete(request, question_id):
    post = get_object_or_404(Question, pk=question_id)

    if request.POST['password'] == post.password:
        post.delete()
        return redirect('question_list')
    else:
        return redirect('question_detail', question_id)

def question_edit(request, question_id):
    post = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.writer = request.POST['writer']
        if request.POST['password'] == post.password:
            post.save()
        return redirect('question_detail', question_id)
    return render(request, 'question_edit.html', {'post': post})

def comment(request, question_id):
    post = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.pub_date = timezone.now()
            comment.question = post
            comment.save()
            return redirect('question_detail', question_id)
        else:
            return redirect('question_detail', question_id)    

def comment_delete(request, question_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'POST':
        if request.POST['password'] == comment.password:
            comment.delete()
            return redirect('question_detail', question_id)
        else:
            return redirect('question_detail', question_id)
    return render(request, 'comment_delete.html')