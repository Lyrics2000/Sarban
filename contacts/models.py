from django.db import models

# Create your models here.

class Contacts(models.Model):
    full_name = models.CharField(max_length=150)
    email_address = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.CharField(max_length=150)
    
    def __str__(self):
        return str(self.full_name)
    
    
