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