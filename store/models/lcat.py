from django.db import models

class Lcat(models.Model):
    name = models.CharField(max_length = 2000)

    @staticmethod
    def get_all_lcats():
        return Lcat.objects.all

    def __str__(self):
        return self.name