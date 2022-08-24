from django.db import models

class Item(models.Model):
    name = models.TextField(max_length=191)
    price = models.TextField(max_length=50)
