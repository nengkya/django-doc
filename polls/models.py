from django.db import models
from django.db.models import Model, CharField
from django.utils import timezone
import datetime

# Create your models here.
class Question(Model):
    question_text = CharField(max_length = 200)
    pub_date = models.DateTimeField('date published');

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

    def __str__(self):
        return self.question_text

class Choice(Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    vote = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text
