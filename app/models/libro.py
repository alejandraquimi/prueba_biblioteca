from django.db import models
class Libro(models.Model):
    codigo=models.CharField(max_length=50)
    titulo=models.CharField(max_length=50)
    autor=models.CharField(max_length=200)
    cantidad_disponible=models.IntegerField()
    fechaRegistro = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'libro'
