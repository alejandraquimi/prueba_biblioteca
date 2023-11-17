from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    template_name = 'biblioteca/login.html'  # Especifica la plantilla que quieres usar

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.user.is_authenticated:
            return redirect('home')  # Redirige a la página de inicio después de iniciar sesión
        return response
