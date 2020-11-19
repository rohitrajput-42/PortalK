from django.db import models

class Icat(models.Model):
    name = models.CharField(max_length = 2000)

    @staticmethod
    def get_all_icats():
        return Icat.objects.all

    def __str__(self):
        return self.name