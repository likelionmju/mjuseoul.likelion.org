from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    writer = models.CharField(max_length=10)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Comment(models.Model): #댓글 모델
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField('date published')
    content = models.TextField()
    writer = models.CharField(max_length=10)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.content