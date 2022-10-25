from django.db import models

# Create your models here.
# Create your models here.

# image class
class Image(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    tags = models.TextField()
    pic = models.FileField(upload_to="pic/%y/")
    def __str__(self):
        return self.title


#  About image class
class About(models.Model):
    title = models.CharField(max_length=150)
    details = models.TextField()
    pic = models.FileField(upload_to="about/%y/")
    def __str__(self):
        return self.title

#  About image class
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    details = models.TextField()
    def __str__(self):
        return self.name