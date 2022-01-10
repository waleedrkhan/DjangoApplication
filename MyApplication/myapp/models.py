from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Person(models.Model):
    GENDERS = (
    ("M", "Male"),
    ("F", "Female"),
    )
    f_name = models.CharField(max_length=25)
    l_name = models.CharField(max_length=25)
    gender = models.CharField(max_length = 1, choices = GENDERS, default = 'M')
