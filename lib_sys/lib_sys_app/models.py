from django.db import models

# Create your models here.
class reader(models.Model):
    def __str__(self):
        return self.reader_name
    reference_id = models.CharField(max_length=200)
    reader_name = models.CharField(max_length=200)
    reader_contact = models.CharField(max_length=200)
    reader_address = models.TextField()
    active = models.BooleanField(default=True)


class book(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    year = models.IntegerField(max_length=200)
    image = models.ImageField(upload_to='static/', default='book-image.jpg') 

class user (models.Model):
    def __str__(self):
        return self.user_username
    user_username = models.CharField(max_length=255)
    user_password = models.CharField(max_length=16)
    user_firstname =  models.CharField(max_length=255)
    user_lastname =  models.CharField(max_length=255)
    user_mail =  models.CharField(max_length=255)