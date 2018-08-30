import datetime

from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=299)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.question_text

    def if_published_recently(self):
        return self.pub_date >= datetime.date.today() - datetime.timedelta(days=2)


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    question = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True, blank=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


