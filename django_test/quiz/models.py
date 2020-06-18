from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    points = models.IntegerField()

    def __str__(self):
        return self.question_text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField()

    def __str__(self):
        return self.choice_text


# Create your models here.
