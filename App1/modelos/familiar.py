from django.db import models
import datetime

class familiar(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    nombre = models.CharField(max_length=100, null=False)
    edad = models.IntegerField(null=False)
    fecha_naciemiento = models.DateField(null=False)


    @classmethod 
    def create(self, nombre:str, edad: int, fecha_naciemiento: datetime.date):
        return self(nombre = nombre,edad = edad, fecha_naciemiento = fecha_naciemiento)
