from django.db import models

# Create your models here.

class Point(models.Model):
    username = models.CharField('Usuario',max_length=70)
    level = models.CharField('Level',max_length=70)

    def __str__(self):
        return f'{self.username}- level:{self.level}'