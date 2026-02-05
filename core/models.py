from django.db import models

class Aircraft(models.Model):
    image = models.ImageField(upload_to="menus/")
    name = models.CharField(max_length=70)
    year_manufacture = models.PositiveIntegerField()
    raid = models.PositiveIntegerField()
    current_rate = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} (${self.current_rate}) (Налёт: {self.raid})"
