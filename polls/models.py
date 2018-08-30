from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=299)
    pub_date = models.DateField('date published')


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    question = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True, blank=True)
    votes = models.IntegerField(default=0)


