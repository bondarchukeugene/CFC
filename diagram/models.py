from django.db import models

class Possesion (models.Model):

    mother = models.CharField (max_length=20)
    child = models.CharField (max_length=20)
    share = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return  self.mother

