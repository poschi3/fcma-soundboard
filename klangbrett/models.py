from django.db import models

class Klang(models.Model):
    displayname = models.CharField(max_length=200)
    file = models.FileField(upload_to='media')
