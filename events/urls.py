"""events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from assitents.views import ParticipantesListado, ParticipanteDetalle, ParticipanteCrear, ParticipanteActualizar, ParticipanteEliminar
from assitents.views import EventosListado, EventoDetalle, EventoCrear, EventoActualizar, EventoEliminar

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('participantes/', ParticipantesListado.as_view(template_name = "participantes/index.html"), name='leer'),
    path('participantes/detalle/<int:pk>', ParticipanteDetalle.as_view(template_name = "participantes/detalles.html"), name='detalles'),
    path('participantes/crear', ParticipanteCrear.as_view(template_name = "participantes/crear.html"), name='crear'),
    path('participantes/editar/<int:pk>', ParticipanteActualizar.as_view(template_name = "participantes/actualizar.html"), name='actualizar'),
    path('participantes/eliminar/<int:pk>', ParticipanteEliminar.as_view(), name='eliminar'),

    path('eventos/', EventosListado.as_view(template_name = "eventos/index.html"), name='leer'),
    path('eventos/detalle/<int:pk>', EventoDetalle.as_view(template_name = "eventos/detalles.html"), name='detalles'),
    path('eventos/crear', EventoCrear.as_view(template_name = "eventos/crear.html"), name='crear'),
    path('eventos/editar/<int:pk>', EventoActualizar.as_view(template_name = "eventos/actualizar.html"), name='actualizar'),
    path('eventos/eliminar/<int:pk>', EventoEliminar.as_view(), name='eliminar'),

]
