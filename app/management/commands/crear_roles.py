# En mi_app/management/commands/crear_roles.py

from django.core.management.base import BaseCommand
from app.models import Rol

class Command(BaseCommand):
    help = 'Crea roles de ejemplo en la base de datos'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creando roles...'))

        

        # Crear roles de ejemplo
        Rol.objects.create(nombre='ADMINISTRADOR')
        Rol.objects.create(nombre='ESTUDIANTE')

        self.stdout.write(self.style.SUCCESS('Roles creados con éxito!'))
