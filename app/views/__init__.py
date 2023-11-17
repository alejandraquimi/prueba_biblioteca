
from .login import CustomLoginView
from .home import HomeView
# En el archivo views/other_views.py o cualquier otro archivo que lo necesite
from .prestamo_libro import prestamo_confirmar_view

__all__ = ["CustomLoginView","HomeView","prestamo_confirmar_view"]