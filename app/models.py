from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    subject = models.CharField(max_length=200,null=True,blank=True)
    message = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
