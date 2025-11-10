from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

class Car(models.Model):
    name = models.CharField(max_length=50, null=False)
    year = models.IntegerField(validators=[MaxValueValidator(2025), MinValueValidator(1900)], null=False)
    description = models.TextField(blank=True, default=";)")

    def __str__(self):
        return f"{self.name} ({self.year})"
    
class LicensePlate(models.Model):
    license_plate = models.CharField(max_length=7, validators=[MinLengthValidator(5)])

    car = models.OneToOneField(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.car} - ({self.license_plate})"
    
class Album(models.Model):
    name = models.CharField(max_length=100, null=False)
    year = models.IntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2025)], null=False)
    music_type = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True, default=";{")

    def __str__(self):
        return f'{self.name} ({self.year})'
    
class Song(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(blank=True, default="Nice song ;)")

    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} (Album - {self.album})"
    

class Team(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(blank=True, default="hewwo")

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=70, null=False)
    surname = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=False,validators=[MaxValueValidator(90), MinValueValidator(14)])

    team = models.ManyToManyField(Team, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} {self.surname}"