from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=255)

class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    year = models.DateField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class Building(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    area = models.DecimalField(max_digits=10, decimal_places=2)      
    floors = models.IntegerField()
    parking = models.BooleanField()
    lift = models.BooleanField()
    playground = models.BooleanField()