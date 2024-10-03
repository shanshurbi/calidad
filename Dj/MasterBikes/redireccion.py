""" UTILIZAR SOLO AL FINAL PARA REDIRECCIONAR A LOS USUARIOS SEGÚN SUS PERMISOS
NO ESTÁ LISTO Y NO ES SEGURO QUE FUNCIONE """

""" EN CASO DE QUE FUNCIONE AGREGAR EN settings.py COMO MIDDLEWARE """

from django.shortcuts import redirect
from django.urls import resolve

class redireccion_cliente:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define las rutas a verificar
        rutas_a_verificar = [
            'ruta_1',  # Reemplaza con el nombre de tu ruta
            'ruta_2',
            'ruta_3',
            'ruta_4',
        ]

        # Verifica si la ruta actual está en la lista de rutas a verificar
        current_route = resolve(request.path_info).url_name
        if request.user.is_authenticated and request.user.username == 'nax' and current_route in rutas_a_verificar:
            return redirect('nueva_url')  # Reemplaza 'nueva_url' con el nombre de la ruta a la que quieres redirigir

        response = self.get_response(request)
        return response
