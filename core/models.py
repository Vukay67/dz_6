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

CATEGOTY_CHOICES = [
    ['Пассажирские', 'Пассажирские'],
    ['Грузовые', 'Грузовые'],
    ['Военно-транспортные', 'Военно-транспортные'],
    ['Боевые', 'Боевые'],
    ['Учебные', 'Учебные'],
    ['Специального назначения', 'Специального назначения'],
]

class AircraftCategory(models.Model):
    categories = models.CharField(choices=CATEGOTY_CHOICES, max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to="categ/")

    def __str__(self):
        return f"{self.categories}"

class Aircraft(models.Model):
    category = models.ForeignKey(AircraftCategory, on_delete=models.CASCADE, related_name="aircraft")
    image = models.ImageField(upload_to="menus/")
    model = models.CharField(max_length=70)
    companys = models.CharField(choices=COMPANY_CHOICES, max_length=20)
    year_manufacture = models.PositiveIntegerField()
    raid = models.PositiveIntegerField()
    current_rate = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.companys}{self.model} (${self.current_rate}) (Налёт: {self.raid})"
