from django.db import models

class Scat(models.Model):
    name = models.CharField(max_length = 2000)

    @staticmethod
    def get_all_scats():
        return Scat.objects.all

    def __str__(self):
        return self.name