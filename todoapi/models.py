from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    competed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title


class Task2(models.Model):
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    competed = models.BooleanField(default=False)

    def __str__(self):
        return self.title