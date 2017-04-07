# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.template import RequestContext
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from models import *
import datetime
import time

def get_consorcios(usuario):
    v = []
    deptos = Departamento.objects.filter(propietario = usuario)
    deptos2 = Departamento.objects.filter(inquilino = usuario)
    if len(deptos) !=0:
        for i in range(len(deptos)):
            v.append(deptos[i].edificio.nombre)
    if len(deptos2) !=0:
        for i in range(len(deptos2)):
            v.append(deptos2[i].edificio.nombre)
    return v

@login_required(login_url='/login')
def index(request):
    exito, error = None, None
    if request.user.is_staff:
        try:
            usuario = request.user
            edificios = Edificio.objects.all()
            edificioSeleccionado  = None
            if request.method == "POST":
                if "selectDepartamento" in request.POST:
                    edificioSeleccionado = Edificio.objects.get(id = request.POST["selectDepartamento"])
                elif "informeCuenta" in request.FILES:
                    informe = request.FILES["informeCuenta"]
                    edificio = Edificio.objects.get(id = request.POST["edificio"])
                    rendicion = RendicionCuenta.objects.create(edificio = edificio, archivo = informe)
                    rendicion.save()
                    for i in range(edificio.departamento_set.all().count()):
                        dpto = Departamento.objects.get(id = edificio.departamento_set.all()[i].id)
                        archivo = request.FILES[str(dpto.id)]
                        expensa = Expensa.objects.create(dpto = dpto, archivo = archivo, rendicion = rendicion)
                        expensa.save()
                        subject, from_email = 'Nueva Expensa Cargada en el Sistema', 'secretaria@criscioneyasociados.com.ar'
                        html_content = 'Hola, desde la administración te informamos que hemos cargado las expensas digitales a través de nuestro portal de internet o haciendo click <a href="http://criscioneyasociados.com.ar/sistema">aquí</a>. Por favor, ingrese ahora para poder descargarlas. Desde ya muchas gracias, Saludos.'
                        msg = EmailMultiAlternatives(subject, '', from_email, [dpto.propietario.email])
                        msg.attach_alternative(html_content, "text/html")
                        msg.send()
                        if dpto.inquilino != None:
                            msg = EmailMultiAlternatives(subject, '', from_email, [dpto.inquilino.email])
                            msg.attach_alternative(html_content, "text/html")
                            msg.send()
                        exito = True
        except:
            error = True
        mensajesNoLeidos = Mensaje.objects.filter(fechaLeido = None).filter(para = usuario).count()
        return render_to_response("indexAdmin.html", {"edificios": edificios, "edificioSeleccionado": edificioSeleccionado, "mensajesNoLeidos": mensajesNoLeidos, "error":error, "exito":exito}, RequestContext(request))
    else:
        expensas = None
        usuario = Persona.objects.get(username = request.user.username)
        departamentos = Departamento.objects.filter(Q(propietario = usuario) | Q(inquilino = usuario))
        mensajesNoLeidos = Mensaje.objects.filter(fechaLeido = None).filter(para = usuario).count()
        if request.method == "POST":
            try:
                departamento = Departamento.objects.get(id = request.POST["selectDepartamento"])
                expensas = departamento.expensa_set.all().order_by('-fecha')[:12]
            except:
                error=True
        return render_to_response("index.html", {"mensajesNoLeidos": mensajesNoLeidos, "departamentos":departamentos, "expensas":expensas, "error":error}, RequestContext(request))

@login_required(login_url='/login')
def enviar_mensaje(request):
    exito, error = None, None
    personas = None
    if request.method == "POST":
        try:
            desde = request.user
            if request.user.is_staff:
                para = Persona.objects.get(id = request.POST["enviarMensajePara"])
            else:
                para = User.objects.get(is_staff = True)
            asunto = request.POST["enviarMensajeAsunto"]
            mensaje = request.POST["enviarMensajeMensaje"]
            archivo = None
            if "enviarMensajeAdjunto" in request.FILES:
                archivo = request.FILES["enviarMensajeAdjunto"]
            enviarMensaje = Mensaje.objects.create(desde = desde, asunto = asunto, mensaje = mensaje, archivo = archivo, para = para)
            enviarMensaje.save()
            subject, from_email = 'Nuevo Mensaje Recibido', 'secretaria@criscioneyasociados.com.ar'
            html_content = 'Hola, desde la administración le informamos que ha recibido un nuevo mensaje a través de nuestro portal de internet o haciendo click <a href="http://criscioneyasociados.com.ar/sistema">aquí</a>. Por favor, ingrese ahora para poder leerlo. Desde ya muchas gracias, Saludos.'
            msg = EmailMultiAlternatives(subject, '', from_email, para.email)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            exito = True
        except:
            error = True
    if request.user.is_staff:
        usuario = request.user
        personas = Persona.objects.filter(is_active = True)
    else:
        usuario = Persona.objects.get(username = request.user.username)
    mensajesNoLeidos = Mensaje.objects.filter(fechaLeido = None).filter(para = usuario).count()
    return render_to_response("enviarMensaje.html", {"personas": personas, "mensajesNoLeidos": mensajesNoLeidos, "error":error, "exito":exito}, RequestContext(request))

@login_required(login_url='/login')
def mensajes(request):
    if request.user.is_staff:
        usuario = request.user
    else:
        usuario = Persona.objects.get(username = request.user.username)
    mensajesNoLeidos = Mensaje.objects.filter(fechaLeido = None).filter(para = usuario).count()
    if request.method == "GET":
        try:
            if "ver" in request.GET:
                mensaje = Mensaje.objects.get(id = request.GET["ver"])
                if mensaje.para == request.user or mensaje.desde == request.user:
                    if mensaje.fechaLeido == None:
                        mensaje.fechaLeido = datetime.datetime.now().date()
                        mensaje.save()
                        mensajesNoLeidos = (mensajesNoLeidos - 1)
                    return render_to_response('verMensaje.html', {"mensaje":mensaje, "mensajesNoLeidos": mensajesNoLeidos}, RequestContext(request))
        except:
            error = True
    mensajes = Mensaje.objects.filter(para = request.user)
    mensajesEnviados = Mensaje.objects.filter(desde = request.user)
    return render_to_response('mensajes.html', {"mensajes":mensajes, "mensajesEnviados":mensajesEnviados, "mensajesNoLeidos": mensajesNoLeidos}, RequestContext(request))

@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render_to_response('cuentaInactiva.html', {}, context)
        else:
            return render_to_response('login.html', {'error':True}, context)
    else:
        return render_to_response('login.html', {}, context)
    
@login_required(login_url='/login')
def espaciosComunes(request):
    mensajesNoLeidos = Mensaje.objects.filter(fechaLeido = None).filter(para = request.user).count()
    if request.user.is_staff:
        reservas = Reserva.objects.all().order_by("fecha")
        url = request.get_host()
        return render_to_response('espaciosComunes.html',{"mensajesNoLeidos": mensajesNoLeidos, "reservas":reservas,"url":url}, RequestContext(request))
    else:
        usuario = Persona.objects.get(username = request.user.username)
        consorcios = get_consorcios(usuario)
        espaciosComunes = []
        for i in range(len(consorcios)):
            espacioscom = EspacioComun.objects.filter(edificio__nombre = consorcios[i])
            for h in range(len(espacioscom)):
                espaciosComunes.append(espacioscom[h])

        estados = []
        fecha = None
        hora = None
        if request.method == 'POST':
            fecha = request.POST['fecha']
            fecha = datetime.datetime.strptime(fecha, '%d/%m/%Y').strftime('%Y-%m-%d')
            hora = request.POST['hora']
            for espacioCom in espaciosComunes:
                estado = espacioCom.get_reserva(fecha,int(hora))
                est_esp = [espacioCom,estado]
                estados.append(est_esp)
            if estados == []:
                estados = "Vacio"
        if not fecha == None:
            fecha = str(fecha)
            fecha = datetime.datetime.strptime(fecha, '%Y-%m-%d').strftime('%d/%m/%Y')
        return render_to_response('espaciosComunes.html',{"mensajesNoLeidos": mensajesNoLeidos, "estados":estados, "fecha":fecha, "hora":hora}, RequestContext(request))

def guardarReserva(request):
    if request.method == 'POST':
        if request.is_ajax():
            usuario = Persona.objects.get(username = request.user.username)
            id_espcom = request.POST.get('id_espacio')
            fecha = request.POST.get('fecha')
            hora = request.POST.get('hora')
            cant_horas = request.POST.get('cant_horas')
            espacioCom = EspacioComun.objects.get(id__exact=id_espcom)
            hs = int(hora)
            hs_fin = hs + int(cant_horas)
            f = datetime.datetime.strptime(fecha, '%d/%m/%Y').strftime('%Y-%m-%d')
            for j in range(hs,hs_fin):
                band = 0
                if j >= 24:
                    hs2 = j - 24
                    f = datetime.datetime.strptime(f, '%Y-%m-%d') + datetime.timedelta(days=1)
                    f = f.strftime('%Y-%m-%d')
                    band = espacioCom.get_reserva(f,hs2)
                else:
                    band = espacioCom.get_reserva(f,j)
                if band != True:
                    data = {'modal':espacioCom.id,'error':"El espacio esta reservado en el horario que lo desea reservar por favor revea la cantidad de horas"}
                    return JsonResponse(data)
            for i in range(hs,hs_fin):
                if i >= 24:
                    hs2 = i-24
                    f = datetime.datetime.strptime(f, '%Y-%m-%d') + datetime.timedelta(days=1)
                    f = f.strftime('%Y-%m-%d')
                    reserva = Reserva.objects.create(espacioComun = espacioCom, persona = usuario, fecha = f, hora = hs2)
                    reserva.save()
                else:
                    reserva = Reserva.objects.create(espacioComun = espacioCom, persona = usuario, fecha = f, hora = i)
                    reserva.save()
            return JsonResponse({'modal':espacioCom.id,'error':"La reserva se a guardado con exito"})
        
@login_required(login_url='/login')
def numerosUtiles(request):
    mensajesNoLeidos = Mensaje.objects.filter(fechaLeido = None).filter(para = request.user).count()
    if request.user.is_staff:
        url = request.get_host()
        numeros = NumeroUtil.objects.all()
        return render_to_response('numerosUtiles.html', {"mensajesNoLeidos": mensajesNoLeidos,"numeros":numeros, "url":url}, RequestContext(request))
    else:
        usuario = request.user
        consorcios = get_consorcios(usuario)
        numeros = []
        for i in range(len(consorcios)):
            edificio = consorcios[i]
            con_num = NumeroUtil.objects.filter(edificio__nombre = edificio)
            for j in range(len(con_num)):
                numeros.append(con_num[j])
        return render_to_response('numerosUtiles.html', {"mensajesNoLeidos": mensajesNoLeidos,"numeros":numeros}, RequestContext(request))
    
@login_required(login_url='/login')
def archivosImportantes(request):
    mensajesNoLeidos = Mensaje.objects.filter(fechaLeido = None).filter(para = request.user).count()
    if request.user.is_staff:
        url = request.get_host()
        archivos = ArchivoImportante.objects.all()
        return render_to_response('archivosImportantes.html', {"mensajesNoLeidos": mensajesNoLeidos,"archivos":archivos,"url":url}, RequestContext(request))
    else:
        usuario = request.user
        consorcios = get_consorcios(usuario)
        archivos = []
        for i in range(len(consorcios)):
            edificio = consorcios[i]
            arch = ArchivoImportante.objects.filter(edificio__nombre = edificio)
            for j in range(len(arch)):
                archivos.append(arch[j])
        return render_to_response('archivosImportantes.html', {"mensajesNoLeidos": mensajesNoLeidos,"archivos":archivos}, RequestContext(request))
    
"""def directorio(request):
    mensajesNoLeidos = Mensaje.objects.filter(fechaLeido = None).filter(para = request.user).count()
    usuario = request.user
    consorcios = get_consorcios(usuario)
    return render_to_response('directorio.html', {"mensajesNoLeidos": mensajesNoLeidos,"archivos":archivos}, RequestContext(request))"""

def configuracion(request):
    edificios = Edificio.objects.all()
    if request.method == "POST":
        if "selectDepartamento" in request.POST:
            edificioSeleccionado = Edificio.objects.get(id = request.POST["selectDepartamento"])
            tiposUnidades = TipodeUnidad.objects.filter(edificio = edificioSeleccionado)
            url = request.get_host()
            tiposGastos = TipodeGastos.objects.filter(edificio = edificioSeleccionado)
            unidades = Unidad.objects.filter(edificio = edificioSeleccionado)
            un_por = []
            for unidad in unidades:
                por = Porcentuales.objects.filter(unidad = unidad).order_by('gasto')
                up = [unidad,por]
                un_por.append(up)
            
            return render_to_response('configuracion.html', {"edificioSeleccionado": edificioSeleccionado, "edificios":edificios, "tiposUnidades":tiposUnidades, "url":url, "tiposGastos":tiposGastos, "unidades":unidades, "un_por":un_por}, RequestContext(request))
        if request.is_ajax():
            if "addTU" in request.POST:
                nombre = request.POST.get('nombre')
                edid = request.POST.get('edificio')
                band = TipodeUnidad.objects.filter(nombre = nombre)
                if not band:
                    edificio = Edificio.objects.get(id = edid)
                    unidad = TipodeUnidad.objects.create(nombre = nombre, edificio = edificio)
                    unidad.save()
                    return JsonResponse({'error':"El tipo de unidad se guardo con exito",'id':unidad.id})
                else:
                    return JsonResponse({'error':"No se pudo guardar este tipo de unidad por que ya hay una con ese nombre"})
            elif "TU" in request.POST:
                TUid = request.POST.get('id')
                TU = TipodeUnidad.objects.get(id__exact = TUid)
                TU.delete()
                return JsonResponse({'error':"El tipo de unidad se elimino con exito",'id':TUid})
            elif "TG" in request.POST:
                TGid = request.POST.get('id')
                TG = TipodeGastos.objects.get(id__exact = TGid)
                TG.porcentajeA = request.POST.get('porA')
                TG.porcentajeB = request.POST.get('porB')
                TG.porcentajeC = request.POST.get('porC')
                TG.porcentajeD = request.POST.get('porD')
                TG.save()
                return JsonResponse({'error':"El tipo de gasto se modifico con exito"})
            elif "nTG" in request.POST:
                por = [request.POST.get('porA'),request.POST.get('porB'),request.POST.get('porC'),request.POST.get('porD')]
                nombre = request.POST.get('nombre')
                band = TipodeGastos.objects.filter(nombre = nombre)
                if not band:
                    edificio = Edificio.objects.get(id__exact = request.POST.get('nTG'))
                    gasto = TipodeGastos.objects.create(nombre = nombre, edificio = edificio, porcentajeA = por[0], porcentajeB = por[1], porcentajeC = por[2], porcentajeD = por[3])
                    gasto.save()
                    return JsonResponse({'error':"El tipo de gasto se guardo con exito"})
                else:
                    return JsonResponse({'error':"No se pudo guardar este tipo de gasto por que ya hay uno con ese nombre"})
            elif "rmvTG" in request.POST:
                TG = TipodeGastos.objects.get(id__exact = request.POST.get('id'))
                TG.delete()
                return JsonResponse({'error':"El tipo de gasto se elimino con exito",'id':request.POST.get('id')})
    return render_to_response('configuracion.html', {"edificios": edificios}, RequestContext(request))

def crear_porcentuales(porcentuales,unidad):
    a = 'ABCDEFGH'
    for i in range(8):
        porcentual = Porcentuales.objects.create(unidad = unidad, porcentual = porcentuales[i], gasto = a[i])
        porcentual.save()

def definir_porcentual(tipo_unidad, porcentual, unidad):
    porcentuales = [0,0,0,0,0,0,0,0,0]
    if tipo_unidad.nombre == "Departamento":
        porcentuales[0] = float(porcentual)
    elif tipo_unidad.nombre == "Oficina":
        porcentuales[1] = float(porcentual)
    elif tipo_unidad.nombre == "Cochera":
        porcentuales[2] = float(porcentual)
    crear_porcentuales(porcentuales,unidad)
        
def agregar(request):
    edificios = Edificio.objects.all()
    if request.method == "POST":
        if "selectDepartamento" in request.POST:
            edificioSeleccionado = Edificio.objects.get(id__exact = request.POST["selectDepartamento"])
            unidades = Unidad.objects.filter(edificio = edificioSeleccionado)
            personas = Persona.objects.filter(edificios = edificioSeleccionado)
            tiposUnidades = TipodeUnidad.objects.filter(edificio = edificioSeleccionado)
            url = request.get_host()
            return render_to_response('agregar.html', {"edificioSeleccionado": edificioSeleccionado,'edificios':edificios, 'unidades':unidades, 'personas':personas,'TUs':tiposUnidades, "url":url}, RequestContext(request))
        if request.is_ajax():
            if "tipoUnidad" in request.POST:
                band = Unidad.objects.filter(ph = request.POST.get('PH'))
                if not band:
                    propietario = Persona.objects.get(id__exact = request.POST.get('propietario'))
                    inquilino = None
                    if request.POST.get('inquilino') != "None":
                        inquilino = Persona.objects.get(id__exact = request.POST.get('inquilino'))
                    edificio = Edificio.objects.get(id__exact = request.POST["edificio"])
                    tipoUnidad = TipodeUnidad.objects.get(id__exact = request.POST["tipoUnidad"])
                    unidad = Unidad.objects.create(edificio = edificio, ph = request.POST.get('PH'), porcentual = float(request.POST.get('porcentual')), depto = request.POST.get('Depto'), tipodeunidad = tipoUnidad, propietario = propietario, inquilino = inquilino)
                    unidad.save()
                    definir_porcentual(tipoUnidad,request.POST.get('porcentual'),unidad)
                    un = Unidad.objects.get(edificio = edificio, ph = request.POST.get('PH'), porcentual = float(request.POST.get('porcentual')), depto = request.POST.get('Depto'), tipodeunidad = tipoUnidad, propietario = propietario, inquilino = inquilino)
                    un = un.id
                    if inquilino != '':
                        return JsonResponse({'error':"Se cargo correctamente la unidad...", 'unidad':un, 'prop':propietario.get_full_name(), 'inq':'---'})
                    else:
                        return JsonResponse({'error':"Se cargo correctamente la unidad...", 'unidad':un, 'prop':propietario.get_full_name(), 'inq':inquilino.get_full_name()})
                else:
                    return JsonResponse({'error':"Ya existe una unidad con ese PH..."})
            elif "GU" in request.POST:
                band = Unidad.objects.filter(ph = request.POST.get('PH')).exclude(id__exact = request.POST.get('id')).count()
                if band == 0:
                    propietario = Persona.objects.get(id__exact = request.POST.get('propietario'))
                    inquilino = None
                    inq = [None," "]
                    if request.POST.get('inquilino') != "None":
                        inquilino = Persona.objects.get(id__exact = request.POST.get('inquilino'))
                        inq = [inquilino.id,inquilino.get_full_name()]
                    unidad = Unidad.objects.get(id__exact = request.POST.get('id'))
                    unidad.ph = request.POST.get('PH')
                    unidad.depto = request.POST.get('Depto')
                    unidad.propietario = propietario
                    unidad.inquilino = inquilino
                    unidad.save()
                    data = {"error":"Unidad modificada con exito...","unidad":{"id":unidad.id,"propietario":{"id":unidad.propietario.id, "nombre":unidad.propietario.get_full_name()},"inquilino":{"id":inq[0],"nombre":inq[1]},"ph":unidad.ph,"depto":unidad.depto}}
                    return JsonResponse(data)
                else:
                    return JsonResponse({'error':"Ya existe una unidad con ese PH..."})
            elif "EU" in request.POST:
                unidad = Unidad.objects.get(id__exact = request.POST.get('id'))
                unidad.delete()
                return JsonResponse({'error':"La Unidad se elimino con exito..."})
            elif "addUser" in request.POST:
                band = Persona.objects.filter(username = request.POST.get('user')).count()
                band1 = Persona.objects.filter(email = request.POST.get('email')).count()
                if band == 0 and band1 == 0:
                    persona = Persona.objects.create(username = request.POST.get('user'), first_name = request.POST.get('nombre'), last_name = request.POST.get('apellido'), email = request.POST.get('email'), telefono = request.POST.get('tel'), telefono2 = request.POST.get('tel2'), direccion = request.POST.get('dir'), password = request.POST.get('pass'))
                    persona.save()
                    edificio = Edificio.objects.get(id__exact = request.POST.get('edificio'))
                    persona.edificios.add(edificio)
                    url = request.get_host()
                    data = {"error":"Persona agregada con exito...","persona":{"id":persona.id,"nombre":persona.first_name, "apellido":persona.last_name, "user":persona.get_username(), "email":persona.email, "dir":persona.direccion, "tel":persona.telefono, "tel2":persona.telefono2, "pass":persona.password},"url":url}
                    return JsonResponse(data)
                else:
                    return JsonResponse({'error':"Ya existe una persona con ese nombre de usuario o email"})
            elif "modUser" in request.POST:
                persona = Persona.objects.get(id__exact = request.POST.get('id'))
                data = {"persona":{"nombre":persona.first_name, "apellido":persona.last_name, "user":persona.get_username(), "email":persona.email, "dir":persona.direccion, "tel":persona.telefono, "tel2":persona.telefono2}}
                return JsonResponse(data)
            elif "guaUser" in request.POST:
                band = Persona.objects.filter(username = request.POST.get('username')).exclude(id__exact = request.POST.get('id')).count()
                band1 = Persona.objects.filter(email = request.POST.get('email')).exclude(id__exact = request.POST.get('id')).count()
                if band == 0 and band1 == 0:
                    persona = Persona.objects.get(id__exact = request.POST.get('id'))
                    persona.first_name = request.POST.get('nombre')
                    persona.last_name = request.POST.get('apellido')
                    persona.username = request.POST.get('username')
                    persona.email = request.POST.get('email')
                    persona.direccion = request.POST.get('dir')
                    persona.telefono = request.POST.get('tel')
                    persona.telefono2 = request.POST.get('tel2')
                    persona.save()
                    url = request.get_host()
                    data = {"error":"Persona guardada con exito...","persona":{"id":persona.id,"nombre":persona.first_name, "apellido":persona.last_name, "user":persona.get_username()},"url":url}
                    return JsonResponse(data)
                else:
                    return JsonResponse({'error':"Ya existe una persona con ese nombre de usuario o email"})
            elif "rmvUser" in request.POST:
                persona = Persona.objects.get(id__exact = request.POST.get('id'))
                persona.delete()
                return JsonResponse({'error':"La persona ha sido eliminada con exito"})
    return render_to_response('agregar.html', {'edificios':edificios}, RequestContext(request))

def consorcios(request):
    consorcios = Edificio.objects.all()
    if "addConsorcio" in request.POST:
        band = 
    return render_to_response('consorcios.html',{'consorcios':consorcios},RequestContext(request))