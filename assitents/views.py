from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Participante
from .models import Evento
from .models import Beneficio

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

class ParticipantesListado(ListView):
    model = Participante

class ParticipanteCrear(SuccessMessageMixin, CreateView):
    model = Participante
    form = Participante
    fields = "__all__"
    success_message = 'Participante creado correctamente'

    def get_success_url(self):
        return reverse('leer')

class ParticipanteDetalle(DetailView):
    model = Participante

class ParticipanteActualizar(SuccessMessageMixin, UpdateView):
    model = Participante
    form = Participante
    fields = "__all__"
    success_message = 'Participante actualizado correctamente'

    def get_success_url(self):
        return reverse('leer')

class ParticipanteEliminar(SuccessMessageMixin, DeleteView):
    model = Participante
    form = Participante
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Participante eliminado correctamente'
        messages.success (self.request, (success_message))
        return reverse('leer')

class EventosListado(ListView):
    model = Evento

class EventoCrear(SuccessMessageMixin, CreateView):
    model = Evento
    form = Evento
    fields = "__all__"
    success_message = 'Participante creado correctamente'

    def get_success_url(self):
        return reverse('leer')

class EventoDetalle(DetailView):
    model = Evento

class EventoActualizar(SuccessMessageMixin, UpdateView):
    model = Evento
    form = Evento
    fields = "__all__"
    success_message = 'Evento actualizado correctamente'

    def get_success_url(self):
        return reverse('leer')

class EventoEliminar(SuccessMessageMixin, DeleteView):
    model = Evento
    form = Evento
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Evento eliminado correctamente'
        messages.success (self.request, (success_message))
        return reverse('leer')
