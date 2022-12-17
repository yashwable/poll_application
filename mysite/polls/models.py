from django.db import models


class Question (model.Model):
    question_text = model.Charfield(max_length=200)
    pub_date = model.DateTimeField('date published')


class Choice(model.Model):
    question = model.foreignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
