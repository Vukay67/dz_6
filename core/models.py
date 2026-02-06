from django.db import models

COMPANY_CHOICES = [
    ['Airbus', 'Airbus'],
    ['Boeing', 'Boeing'],
    ['Embraer', 'Embraer'],
    ['Bombardier', 'Bombardier'],
    ['ATR', 'ATR'],
    ['Сухой', 'Сухой'],
    ['Иркут', 'Иркут'],
    ['COMAC', 'COMAC'],
    ['Gulfstream', 'Gulfstream'],
    ['Dassault', 'Dassault'],
    ['Cessna', 'Cessna']
]

class Aircraft(models.Model):
    image = models.ImageField(upload_to="menus/")
    model = models.CharField(max_length=70)
    companys = models.CharField(choices=COMPANY_CHOICES, max_length=20)
    year_manufacture = models.PositiveIntegerField()
    raid = models.PositiveIntegerField()
    current_rate = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.companys}{self.model} (${self.current_rate}) (Налёт: {self.raid})"
