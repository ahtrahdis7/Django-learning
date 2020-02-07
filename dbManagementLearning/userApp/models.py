from django.db import models

# Create your models here.
class users(models.Model):
    fname = models.CharField(max_length= 200)
    lname = models.CharField(max_length= 200)
    mail = models.EmailField(max_length= 300, unique = True)

    