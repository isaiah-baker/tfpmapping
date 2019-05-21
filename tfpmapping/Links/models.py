from django.db import models

# Create your models here.

class Link(models.Model):
    link_text = models.CharField(max_length=500)
    link_name = models.CharField(max_length=200)

    def __str__(self):
        return self.link_text
