# En mi_app/management/commands/crear_usuarios.py

from django.core.management.base import BaseCommand
from app.models import User, Rol

class Command(BaseCommand):
    help = 'Crea usuarios de ejemplo en la base de datos'


    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creando usuarios...'))
        rol_estudiante = Rol.objects.get(nombre='ESTUDIANTE')
        rol_administrador=Rol.objects.get(nombre='ADMINISTRADOR')

        # Crear usuarios de ejemplo
        User.objects.create_user(username='administrador',email="admin@hotmail.com", password='admin',rol=rol_administrador)

        User.objects.create_user(username='estudiante1',email="qal@hotmail.com", password='estudiante1',rol=rol_estudiante)
        User.objects.create_user(username='estudiante2',email="est@hotmail.com", password='estudiante2',rol=rol_estudiante)

        self.stdout.write(self.style.SUCCESS('Usuarios creados con éxito!'))
