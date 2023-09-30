from django.db import models

# Create your models here.
class Agenda(models.Model):
    atv1 = models.CharField(max_length=50)
    atv2 = models.CharField(max_length=50)
    atv3 = models.CharField(max_length=50)
    atv4 = models.CharField(max_length=50)
    atv5 = models.CharField(max_length=50)
    atv6 = models.CharField(max_length=50)
    atv7 = models.CharField(max_length=50)
    atv8 = models.CharField(max_length=50)
    user = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user
