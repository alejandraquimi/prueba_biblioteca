from django.db import models
from app.models import Libro, User
class Prestamo(models.Model):
    usuario=models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    libro=models.ForeignKey(Libro,on_delete=models.SET_NULL, null=True)
    fecha_emision=models.DateField(null=True)
    fecha_devolucion=models.DateField(null=True)
    reservado=models.BooleanField(null=True)
    confirmado=models.BooleanField(null=True)
    devuelto=models.BooleanField(null=True)
    class Meta:
        db_table = 'prestamo'
