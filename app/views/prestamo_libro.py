from django.http import JsonResponse
from django.views.decorators.http import require_POST
from app.models import Prestamo
from datetime import datetime, timedelta
from django.shortcuts import render, redirect

@require_POST
def prestamo_confirmar_view(request):
    print(f"libro reservado")

    try:
        cancelar = request.POST.get('cancelar_prestamo','')

        prestamo = Prestamo.objects.get(usuario=request.user, reservado=True, confirmado=False)


        if(cancelar!=''):
            prestamo.libro.cantidad_disponible += 1
            prestamo.libro.save()
            prestamo.delete()
        else:
            prestamo.confirmado = True
            prestamo.fecha_emision = datetime.now()
            prestamo.fecha_devolucion = prestamo.fecha_emision + timedelta(days=30)
            prestamo.reservado=False
            prestamo.devuelto=False
            prestamo.save()



        return redirect("home")
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})
