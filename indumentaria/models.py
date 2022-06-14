from django.db import models

class Remera(models.Model):
    marca = models.CharField("Marca" , max_length=30)
    TALLES = (
        (1, "XS"),
        (2, "S"),
        (3, "M"),
        (4, "L"),
        (5, "XL"),
        (6, "XXL")
    )
    talle = models.PositiveSmallIntegerField("Talle", choices=TALLES)
    color = models.CharField("Color", max_length=15)
    precio = models.FloatField("Precio $")
