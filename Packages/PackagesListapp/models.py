from django.db import models

# Create your models here.

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)

class Package(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # Add other fields as needed

    def __str__(self):
        return self.name


class CarWashService(models.Model):
  """
  A class representing a car wash service offered by Aplus.
  """
  def __init__(self, name, description, price):
    self.name = name
    self.description = description
    self.price = price

# Define some example car wash services
full_clean = CarWashService("Full Clean", "Includes interior vacuuming, window cleaning, and a thorough hand wash.", 49.99)
exterior_wash = CarWashService("Exterior Wash", "Provides a high-gloss exterior wash and tire shine.", 29.99)
interior_detail = CarWashService("Interior Detail", "Deep cleans carpets, upholstery, and dashboards.", 39.99)

# List of services offered
services = [full_clean, exterior_wash, interior_detail]

