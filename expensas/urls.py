# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from consorcios import settings
import views

urlpatterns = [
    url(r'^$', views.index, name='inicio'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^enviar_mensaje/', views.enviar_mensaje, name='enviarMensaje'),
    url(r'^mensajes/', views.mensajes, name='mensajes'),
    url(r'^espaciosComunes/', views.espaciosComunes, name='espaciosComunes'),
    url(r'^guardarReserva/', views.guardarReserva, name='guardarReserva'),
    url(r'^numerosUtiles/', views.numerosUtiles, name='numerosUtiles'),
    url(r'^archivosImportantes/', views.archivosImportantes, name='archivosImportantes'),
    url(r'^configuracion/', views.configuracion, name='configuracion'),
    url(r'^agregar/', views.agregar, name='agregar'),
    url(r'^consorcios/', views.consorcios, name='consorcios'),
#    url(r'^directorio/', views.directorio, name='directorio'),
#    url(r'^contacto/', views.contacto, name='contacto'),
#    url(r'^recuperar/', views.recuperar, name='recuperar'),
#    url(r'^verificar_numero/', views.verificarNumero, name='verificarNumero'),
#    url(r'^reenviar_email/', views.reenviarEmail, name='reenviarEmail'),
#    url(r'^cambiar_pregunta/', views.cambiarPregunta, name='cambiarPregunta'),
#    url(r'^cambiar_email/', views.cambiarEmail, name='cambiarEmail'),
#    url(r'^cambiar_password/', views.cambiarPassword, name='cambiarPassword'),
#    url(r'^notificaciones_pagos/', views.notificacionesPagos, name='notificacionesPagos'),
#    url(r'^perfil_consumidor/', views.perfilConsumidor, name='perfilConsumidor'),
#    url(r'^favoritos_consumidor/', views.favoritosConsumidor, name='favoritosConsumidor'),
#    url(r'^sucursal_consumidor/', views.sucursalConsumidor, name='sucursalConsumidor'),
#    url(r'^sucursal_adminstrada/', views.sucursalAdministrada, name='sucursalAdministrada'),
#    url(r'^beneficios_consumidor/', views.beneficiosConsumidor, name='beneficiosConsumidor'),
#    url(r'^busqueda/', views.busquedaConsumidor, name='busqueda'),
]