from django.db import models

class Skillcat(models.Model):
    name = models.CharField(max_length = 2000)

    @staticmethod
    def get_all_skillcats():
        return Skillcat.objects.all

    def __str__(self):
        return self.name