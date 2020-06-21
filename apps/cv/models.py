import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.db import models
from django.utils import timezone


def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Cv(models.Model):
    cv_filename = models.CharField(max_length=200)
    published_Date = models.DateTimeField(blank=True, null=True)
    cv_File = models.FileField(upload_to="gallery", blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.cv_filename





