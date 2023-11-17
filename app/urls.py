from django.urls import path
from .views import CustomLoginView,HomeView,prestamo_confirmar_view

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),  
    path('login/', CustomLoginView.as_view(), name='login'),  
    path('home/', HomeView.as_view(), name='home'),
    path('prestamo_confirmar/', prestamo_confirmar_view, name='prestamo_confirmar'),
  ]