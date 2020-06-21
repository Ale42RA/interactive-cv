import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.db import models
from django.utils import timezone


class Me(models.Model):
    my_Name = models.CharField(max_length=100, blank=True)
    my_Level = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(99), MinValueValidator(0)], 
        blank=True
     )
    my_Introduction = models.TextField(blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.my_Name
    


SKILL_LEVEL_CHOICES = (
    ('Beginner','Beginner'),
    ('Average', 'Average'),
    ('Skilled','Skilled'),
    ('Specialist','Specialist'),
    ('Expert','Expert'),
)

SKILL_TYPE = (
    ('Script or Programming Languages','Script or Programming Languages'),
    ('Other','Other'),
    
)

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Skillset(models.Model):
    skill_Title = models.CharField(max_length=200, blank=True)
    skill_Description = models.TextField(blank=True)
    skill_Level =models.CharField(max_length=16, choices=SKILL_LEVEL_CHOICES, default='Beginner', blank=True)
    skill_Type =models.CharField(max_length=90, choices=SKILL_TYPE, default='Other', blank=True)
    year_Started = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(2015), max_value_current_year], blank=True)
    def __str__(self):
        return self.skill_Title

class Equipment(models.Model):
    equipment_Name = models.CharField(max_length=200, blank=True)
    equipment_Description = models.TextField(blank=True)
    def __str__(self):
        return self.equipment_Name

class Attribute(models.Model):
    attribute_Name = models.CharField(max_length=200, blank=True)
    attribute_Level = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(10), MinValueValidator(0)],
        blank=True
     )
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.attribute_Name

class WorkExp(models.Model):
    work_Exp_Title = models.CharField(max_length=200, blank=True)
    work_Exp_Company = models.CharField(max_length=200, blank=True)
    work_Exp_Description = models.TextField(blank=True)
    year_Started = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(2015), max_value_current_year], blank=True)
    year_Finished = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(2015), max_value_current_year], blank=True)
    published_Date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.work_Exp_Title

class Education(models.Model):
    degree_Title = models.CharField(max_length=200, blank=True)
    institute_Name = models.CharField(max_length=200, blank=True)
    year_Gained = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(2015), max_value_current_year], blank=True)
    published_date = models.DateTimeField(blank=True, null=True)
    degree_completed = models.BooleanField(default=True)

    def years(self):
        return timezone.now() - self.created_date()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.degree_Title

class Like(models.Model):
    like_Title = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.like_Title

