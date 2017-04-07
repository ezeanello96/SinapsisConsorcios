# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Edificio(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    direccion = models.CharField("Dirección", max_length=50)
    observaciones = models.CharField("Observaciones", max_length=250, null=True, blank=True)
    fondoDeReserva = models.FloatField("Fondo de Reserva", blank=True)
    
    class Meta:
        verbose_name = 'Edificio / Consorcio'
        verbose_name_plural = 'Edificios / Consorcios'
        ordering = ("nombre",)
        
    def __unicode__(self):
	    return self.nombre
    
class Persona(User):
    telefono = models.CharField("Teléfono", max_length=30, null=True, blank=True)
    telefono2 = models.CharField("Teléfono 2", max_length=30, null=True, blank=True)
    direccion = models.CharField("Dirección", max_length=50, null=True, blank=True)
    edificios = models.ManyToManyField(Edificio)
    
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ("last_name", "first_name",)
        
    def __unicode__(self):
	    return self.last_name.upper() + ", " + self.first_name.capitalize()
    
class RendicionCuenta(models.Model):
    fecha = models.DateField("Fecha", auto_now_add=True)
    archivo = models.FileField("Archivo", upload_to='informes/')
    edificio = models.ForeignKey(Edificio)
    
    class Meta:
        verbose_name = 'Rendición de Cuenta'
        verbose_name_plural = 'Rendiciones de Cuenta'
        ordering = ("fecha",)
        
    def __unicode__(self):
	    return self.edificio.nombre.capitalize() + " - " + str(self.fecha)
    
"""class Expensa(models.Model):
    fecha = models.DateField("Fecha", auto_now_add=True)
    archivo = models.FileField("Archivo", upload_to='expensas/')
    dpto = models.ForeignKey(Departamento)
    rendicion = models.ForeignKey(RendicionCuenta, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Expensa'
        verbose_name_plural = 'Expensas'
        ordering = ("fecha",)
        
    def __unicode__(self):
	    return self.dpto.edificio.nombre.capitalize() + " " + str(self.dpto.piso) + self.dpto.departamento + " - " + str(self.fecha)"""
    
class Mensaje(models.Model):
    fecha = models.DateField("Fecha", auto_now_add=True)
    desde = models.ForeignKey(User, related_name="Remitente")
    para = models.ForeignKey(User, related_name="Destinatario")
    mensaje = models.CharField("Mensaje", max_length=1000)
    asunto = models.CharField("Asunto", max_length=100, null=True)
    fechaLeido = models.DateField("Fecha Leído", null=True, blank=True, default=None)
    archivo = models.FileField("Archivo Adjunto", upload_to='adjuntos/', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
        ordering = ("fecha",)
        
    def __unicode__(self):
	    return "Mensaje de " + self.desde.get_full_name() + " a " +  self.para.get_full_name() + " - " + str(self.fecha)
    
class EspacioComun(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    descripcion = models.CharField("Descripcion", max_length=250)
    edificio = models.ForeignKey(Edificio,null=True,blank=True)
    
    class Meta:
        verbose_name = 'Espacio comun'
        verbose_name_plural = 'Espacios comunes'
        ordering = ("nombre",)
    
    def get_reserva(self, fecha, hora):
        reservas = Reserva.objects.filter(espacioComun = self , fecha = fecha, hora = hora).count()
        if reservas == 0:
            return True
        else:
            reserva = Reserva.objects.get(espacioComun = self , fecha = fecha, hora = hora)
            return reserva
        
class NumeroUtil(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    telefono = models.IntegerField("Telefono")
    servicio = models.CharField("Servicio", max_length=50, null=True, blank=True)
    edificio = models.ManyToManyField(Edificio)
    
    class Meta:
        verbose_name = 'Numero Util'
        verbose_name_plural = 'Numeros Utiles'
        ordering = ("nombre",)
    
class ArchivoImportante(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    archivo = models.FileField("Archivo", upload_to='importantes/', null=True, blank=True)
    fecha = models.DateField("Fecha de subida", auto_now_add=True)
    edificio = models.ForeignKey(Edificio)
    
    class Meta:
        verbose_name = 'Archivo importante'
        verbose_name_plural = 'Archivos importantes'
        ordering = ("nombre",)
        
class Reserva(models.Model):
    horas = ((0,"00"),
             (1,"01"),
             (2,"02"),
             (3,"03"),
             (4,"04"),
             (5,"05"),
             (6,"06"),
             (7,"07"),
             (8,"08"),
             (9,"09"),
             (10,"10"),
             (11,"11"),
             (12,"12"),
             (13,"13"),
             (14,"14"),
             (15,"15"),
             (16,"16"),
             (17,"17"),
             (18,"18"),
             (19,"19"),
             (20,"20"),
             (21,"21"),
             (22,"22"),
             (23,"23"),)
    espacioComun = models.ForeignKey(EspacioComun)
    persona = models.ForeignKey(User)
    fecha = models.DateField("Fecha")
    hora = models.IntegerField("Hora", choices=horas, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ("fecha",)
        
class TipodeGastos(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    porcentajeA = models.IntegerField("Porcentaje A")
    porcentajeB = models.IntegerField("Porcentaje B")
    porcentajeC = models.IntegerField("Porcentaje C")
    porcentajeD = models.IntegerField("Porcentaje D")
    edificio = models.ForeignKey(Edificio)
    
    class Meta:
        verbose_name = 'Tipo de Gastos'
        verbose_name_plural = 'Tipos de Gastos'
        ordering = ("nombre",)
        
class TipodeUnidad(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    edificio = models.ForeignKey(Edificio)
    
    class Meta:
        verbose_name = 'Tipo de Unidad'
        verbose_name_plural = 'Tipos de Unidades'
        ordering = ("nombre",)
    
    def __unicode__(self):
	    return self.edificio.nombre.capitalize() + " - " + self.nombre
    
class Unidad(models.Model):
    edificio = models.ForeignKey(Edificio)
    ph = models.CharField("PH", max_length=4)
    depto = models.CharField("Depto", max_length=5)
    porcentual = models.FloatField("Porcentual (%)")
    tipodeunidad = models.ForeignKey(TipodeUnidad)
    propietario = models.ForeignKey(Persona, related_name="Propietario")
    inquilino = models.ForeignKey(Persona, null=True, blank = True, related_name="Inquilino")
    
    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'
        ordering = ("edificio","ph","tipodeunidad")
        
    def __unicode__(self):
	    return self.edificio.nombre.capitalize() + " - " + self.ph + " - " + self.depto
    
class Porcentuales(models.Model):
    unidad = models.ForeignKey(Unidad)
    gasto = models.CharField("Gasto", max_length=1)
    porcentual = models.FloatField("Porcentual (%)")
    
    class Meta:
        verbose_name = 'Porcentual'
        verbose_name_plural = 'Porcentuales'
        ordering = ("unidad","gasto")
        
    def __unicode__(self):
	    return self.unidad.edificio.nombre.capitalize() + " - " + self.unidad.depto