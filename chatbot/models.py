from django.db import models

class Scheme(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    min_income = models.IntegerField()
    max_income = models.IntegerField()
    category = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.name
