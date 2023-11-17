from django.views.generic import TemplateView
from app.models import Libro,Prestamo
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

class HomeView(TemplateView):
    template_name = 'biblioteca/home.html'  
    def get(self, request, *args, **kwargs):
        try:
            if self.request.user.rol:
                rol_nombre = self.request.user.rol.nombre

            codigo = request.GET.get('codigo', '')

            if codigo:
                libro = get_object_or_404(Libro, codigo=codigo)
                data = {
                    'codigo': libro.codigo,
                    'titulo': libro.titulo,
                    'autor': libro.autor,
                    'cantidad_disponible': libro.cantidad_disponible,
                }
                return JsonResponse(data)
            else:
                user = request.user
                context = self.get_context_data()

                prestamo_agregado= Prestamo.objects.filter(usuario=user,reservado=True)
                if prestamo_agregado:
                    context['boton_reservado']=False
                else:
                    libros = Libro.objects.exclude(
                        prestamo__usuario=self.request.user,
                        prestamo__devuelto=False
                    ).distinct()
                    prestamos = Prestamo.objects.filter(usuario=request.user, devuelto=False)
                    context = self.get_context_data()
                    context['libros'] = libros
                    context['boton_reservado'] = True
                    context ['libros_prestados']= prestamos


                return render(request, self.template_name, context)
        except Exception as e:
            error_message = f'Error al realizar la operación: {str(e)}'
            data={"error":"No existe información"}
            print(error_message)
            return JsonResponse(data)
            
    def post(self, request, *args, **kwargs):
        try:
            codigo = request.POST.get('codigo')
            titulo = request.POST.get('titulo')
            autor = request.POST.get('autor')
            cantidad_disponible = int(request.POST.get('cantidad_disponible', 0))
            reservar_libro = request.POST.get('reservar_libro')
            if reservar_libro:
                user = request.user
                libro = get_object_or_404(Libro, codigo=codigo)

                if libro.cantidad_disponible > 0:
                    libro.cantidad_disponible -= 1
                    libro.save()

                    nuevo_prestamo =Prestamo(usuario=user,libro=libro,fecha_emision=None,reservado=True,confirmado=False,fecha_devolucion=None,devuelto=True)
                    
                    nuevo_prestamo.save()

                    messages.success(request, 'Libro reservado exitosamente.')
                    context = self.get_context_data()
                    context['libro_reservado'] = nuevo_prestamo
                    
                    context['boton_reservado']=False
                
                    return render(request, self.template_name, context)
                else:
                    messages.error(request, 'No hay libros disponibles para reservar.')
                    return redirect("home")
                
            else:
                libro_existente = Libro.objects.filter(codigo=codigo).first()

                if libro_existente:
                    libro_existente.cantidad_disponible += cantidad_disponible
                    libro_existente.save()
                    message = 'Cantidad disponible actualizada exitosamente.'
                else:
                    nuevo_libro = Libro(
                        codigo=codigo,
                        titulo=titulo,
                        autor=autor,
                        cantidad_disponible=cantidad_disponible
                    )
                    nuevo_libro.save()
                    message = 'Libro guardado exitosamente.'

                print("Operación exitosa:", message)
                return redirect('home')

        except Exception as e:
            error_message = f'Error al realizar la operación: {str(e)}'
            print(error_message)
            return JsonResponse({'success': False, 'message': error_message})
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.rol:
            rol_nombre = self.request.user.rol.nombre
            context['rol_nombre'] = rol_nombre

        return context
