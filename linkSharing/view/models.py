from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Link(models.Model):
    link_name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    # user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.url
