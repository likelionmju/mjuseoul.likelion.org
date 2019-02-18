from django.contrib import admin

# Register your models here.
from .models import Question, Comment

admin.site.register(Question)
admin.site.register(Comment)