from django.urls import reverse
from django.db import models

class Root(models.Model):
    # Fields
    Root_Certificate = models.TextField(max_length=200, default='')
    Expiration_date = models.DateField()

class Intermediate(models.Model):

    # Fields
    Intermidiate_Certificate = models.TextField(max_length=200, default='')
    Expiration_date = models.DateField()
	
	# Relationship Fields2
    Root_Certificate = models.ForeignKey(Root, on_delete=models.CASCADE, default='')

class Identity(models.Model):

    # Fields
    Identity_Certificate = models.CharField(Intermediate, max_length=200, default='')
    Expiration_date = models.DateField()

    # Relationship Fields
    Intermidiate_Certificate = models.ForeignKey(Intermediate, on_delete=models.CASCADE, default='')
    Root_Certificate = models.ForeignKey(Root, on_delete=models.CASCADE, default='')

class URL(models.Model):
    # Fields
    AirlineID_VendorID = models.CharField(max_length=3, default='')
    Application_URL = models.URLField(max_length=200, default="test.com",primary_key=True)
	
	# Relationship Fields
    Identity_Certificate = models.ForeignKey(Identity, on_delete=models.CASCADE, default='')

 
