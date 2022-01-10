from django.db import models
from datetime import datetime


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


class Clinic(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)


class TimeSlots(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    startTime = models.TimeField(null=True)
    endTime = models.TimeField(null=True)

class Patients(models.Model):
    name = models.CharField(max_length=255)
    dateAdmitted = models.DateTimeField(default=datetime.now)
    dateCheckOut = models.DateTimeField(null=True)
    doctor = models.ManyToManyField(Doctor)

class Appointments(models.Model):
    STATUS = (
        ("F", "Free"),
        ("P", "Pending"),
        ("C", "Complete"),
        ("F", "Final"),
        ("I", "Incomplete"),
        ("R", "Rejected"),
    )
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    patient = models.OneToOneField(Patients, on_delete=models.CASCADE)
    timeslot = models.OneToOneField(TimeSlots, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS, default='P')
    notes = models.CharField(max_length=255, null=True)