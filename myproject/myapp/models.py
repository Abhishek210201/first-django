from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    attachment = models.FileField(upload_to='contact_files/', blank=True, null=True)

    def __str__(self):
        return self.name    