"""
URL configuration for pedidosonline project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from online.views import portada, detalle_producto, registrarse, iniciar_sesion, registro, ingresar, cerrar_sesion, mi_cuenta

admin.site.site_header = 'Sistema de Pedidos en línea'
admin.site.site_title = 'Sistema de Pedidos en línea'
admin.site.index_title = 'Inicio del sistema'

urlpatterns = [
    path('admin/', admin.site.urls),
    # url para la parte publica
    path('', portada, name="portada"),
    path('detalle_producto/<slug:slug_producto>', detalle_producto, name='detalle_producto'),
    path('registrarse', registrarse, name="registrarse"),
    path('iniciar_sesion', iniciar_sesion, name="iniciar_sesion"),
    path('registro', registro, name='registro'),
    path('ingresar', ingresar, name='ingresar'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),
    path('mi_cuenta', mi_cuenta, name='mi_cuenta'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
