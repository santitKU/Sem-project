from django.db import models

# Create your models here.

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Disease(models.Model):
    title = models.CharField(max_length=100)
    symptoms = models.TextField()

    def __str__(self):
        return self.title

class Input(models.Model):
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)

