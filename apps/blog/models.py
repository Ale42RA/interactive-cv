from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
import os

POST_TYPE = (
    ('Computer Science','Computer Science'),
    ('Art', 'Art'),
    ('Other','Other'),
)

def get_image_path(instance, filename):
    return os.path.join('blog/', filename)

class Post(models.Model):
    post_Title = models.CharField(max_length=200)
    post_Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_Text = models.TextField()
    post_Type =models.CharField(max_length=16, choices=POST_TYPE, default='other')
    post_Assignment = models.BooleanField(default=False)
    published_Date = models.DateTimeField(blank=True, null=True)
    post_Image = models.ImageField(upload_to="gallery", blank=True, null=True)
    post_Body_Image1 = models.ImageField(upload_to="gallery", blank=True, null=True)
    post_Body_Image2 = models.ImageField(upload_to="gallery", blank=True, null=True)
    post_Body_Image3 = models.ImageField(upload_to="gallery", blank=True, null=True)
    post_Body_Image4 = models.ImageField(upload_to="gallery", blank=True, null=True)


    def years(self):
        return timezone.now() - self.created_date()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.post_Title
