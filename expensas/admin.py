# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from models import *

class PersonaAddForm(UserCreationForm):
    class Meta:
        model = Persona
        fields = ('first_name', 'last_name', 'username', 'email', 'direccion', 'telefono', 'telefono2')

        def __init__(self, *args, **kwargs):
            return super(PersonaAddForm,self).__init__( *args, **kwargs)

class PersonaForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(label= ("Password"),
    help_text= ("La contraseña está encriptada y no puede verla.<br />"
                    "Sí puede cambiarla buscando al usuario en la tabla "
                    "siguiente <a href='/admin/auth/user'>click aquí</a>."))
    class Meta:
        model = Persona
        fields = ('first_name', 'last_name', 'username', 'email', 'direccion', 'telefono', 'telefono2')

class PersonaAdmin(admin.ModelAdmin):
    form = PersonaForm
    add_form = PersonaAddForm
    
    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return PersonaAddForm
        else:
            return super(PersonaAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(Edificio)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Unidad)
admin.site.register(EspacioComun)
admin.site.register(Reserva)
admin.site.register(NumeroUtil)
admin.site.register(ArchivoImportante)
admin.site.register(TipodeUnidad)
admin.site.register(TipodeGastos)
admin.site.register(Porcentuales)
#admin.site.register(RendicionCuenta)
#admin.site.register(Expensa)
#admin.site.register(Mensaje)
admin.site.unregister(Group)