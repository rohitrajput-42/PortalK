from django.db import models

class Ecat(models.Model):
    name = models.CharField(max_length = 2000)

    @staticmethod 
    def get_all_ecats():
        return Ecat.objects.all

    def __str__(self):
        return self.name