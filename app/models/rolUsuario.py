from django.db import models
class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    fechaRegistro = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'rol'
