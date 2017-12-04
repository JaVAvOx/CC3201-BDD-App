from django.shortcuts import render
from django.http import HttpResponse
from prueba.models import *
from prueba.models import Mes
from django.db import connection
from collections import namedtuple
from django.shortcuts import render
from .forms import NombreInsumoForm
from .forms import consulta11Form
from .forms import consulta22Form
from .forms import consulta33Form
from .forms import pruebaForm
from .forms import insertarCarro
from .forms import insertarInsumo
from .forms import insertarCliente
from .forms import insertarProveedor
from .forms import actualizarProceso
from .forms import actualizarCarro
from .forms import actualizarInsumo
from .forms import actualizarProveedor
from .forms import actualizarCliente

#index
def index(request):
    #return HttpResponse("Hola, soy una prueba.")
    return render(request,'prueba/base.html')

#pruebas
def tablaprueba(request):
    insumo = Insumos.objects.all()
    contexto = {'tabla': insumo}
    return render(request, 'prueba/indexprueba.html',contexto)

def pruebaformulario(request):
    form = pruebaForm()
    return render(request, 'prueba/formularioprueba.html', {'prueba_form': form})

#actulizar datos
def actualizar_proceso(request):
    if request.method == 'POST':
        form = actualizarProceso(request.POST)
        if form.is_valid():
            id = request.GET.get('id_carro')
            proceso = Proceso.objects.get(id_carro = id)
            proceso.etapa = form.cleaned_data['etapa']
            proceso.hora_ingreso = form.cleaned_data['hora_ingreso']
            proceso.hora_salida = form.cleaned_data['hora_salida']
            proceso.save()
            elemento = generar_tablaProceso()
            contexto = {'tabla': elemento}
            return render(request, 'prueba/tablaProceso.html',contexto)
            #return render(request,'prueba/actualizar.html', {'actualizar_form': form, 'id': id})

    form = actualizarProceso()
    if request.method == 'GET':
        id = request.GET.get('id_carro')
        if not id:
            return render(request,'prueba/actualizar_proceso.html', {'actualizarproceso_form': form})
        else:
            # siempre caemos aqui (por medio del boton)

            return render(request,'prueba/actualizar_proceso.html', {'actualizarproceso_form': form, 'id': id})
    else:
        return render(request,'prueba/actualizar_proceso.html', {'actualizarproceso_form': form,})

def actualizar_carro(request):
    if request.method == 'POST':
        form = actualizarCarro(request.POST)
        if form.is_valid():
            id = request.GET.get('id_carro')
            carro = Carro.objects.get(id_carro = id)
            carro.producto = form.cleaned_data['producto']
            carro.stock = form.cleaned_data['stock']
            carro.estado = form.cleaned_data['estado']
            carro.save()
            elemento = generar_tablaCarro()
            contexto = {'tabla': elemento}
            return render(request, 'prueba/tablaCarro.html',contexto)
            #return render(request,'prueba/actualizar.html', {'actualizar_form': form, 'id': id})

    form = actualizarCarro()
    if request.method == 'GET':
        id = request.GET.get('id_carro')
        if not id:
            return render(request,'prueba/actualizar_carro.html', {'actualizarcarro_form': form})
        else:
            # siempre caemos aqui (por medio del boton)

            return render(request,'prueba/actualizar_carro.html', {'actualizarcarro_form': form, 'id': id})
    else:
        return render(request,'prueba/actualizar_carro.html', {'actualizarcarro_form': form})

def actualizar_proveedor(request):
    if request.method == 'POST':
        form = actualizarProveedor(request.POST)
        if form.is_valid():
            id = request.GET.get('id_compra')
            proveedor = Proveedor.objects.get(id_compra = id)
            proveedor.empresa = form.cleaned_data['empresa']
            proveedor.telefono = form.cleaned_data['telefono']
            proveedor.fecha = form.cleaned_data['fecha']
            proveedor.cantidad = form.cleaned_data['cantidad']
            proveedor.precio = form.cleaned_data['precio']
            proveedor.insumo = form.cleaned_data['insumo']
            proveedor.save()
            elemento = generar_tablaProveedor()
            contexto = {'tabla': elemento}
            return render(request, 'prueba/tablaProveedor.html',contexto)
            #return render(request,'prueba/actualizar.html', {'actualizar_form': form, 'id': id})

    form = actualizarProveedor()
    if request.method == 'GET':
        id = request.GET.get('id_compra')
        if not id:
            return render(request,'prueba/actualizar_proveedor.html', {'actualizarproveedor_form': form})
        else:
            # siempre caemos aqui (por medio del boton)

            return render(request,'prueba/actualizar_proveedor.html', {'actualizarproveedor_form': form, 'id': id})
    else:
        return render(request,'prueba/actualizar_proveedor.html', {'actualizarproveedor_form': form})


def actualizar_cliente(request):
    if request.method == 'POST':
        form = actualizarCliente(request.POST)
        if form.is_valid():
            id = request.GET.get('id_venta')
            cliente = Cliente.objects.get(id_venta = id)
            cliente.nombre_cliente = form.cleaned_data['nombre']
            cliente.telefono = form.cleaned_data['telefono']
            cliente.fecha = form.cleaned_data['fecha']
            cliente.cantidad = form.cleaned_data['cantidad']
            cliente.precio = form.cleaned_data['precio']
            cliente.save()
            elemento = generar_tablaCliente()
            contexto = {'tabla': elemento}
            return render(request, 'prueba/tablaCliente.html',contexto)
            #return render(request,'prueba/actualizar.html', {'actualizar_form': form, 'id': id})

    form = actualizarCliente()
    if request.method == 'GET':
        id = request.GET.get('id_venta')
        if not id:
            return render(request,'prueba/actualizar_cliente.html', {'actualizarcliente_form': form})
        else:
            # siempre caemos aqui (por medio del boton)

            return render(request,'prueba/actualizar_cliente.html', {'actualizarcliente_form': form, 'id': id})
    else:
        return render(request,'prueba/actualizar_cliente.html', {'actualizarcliente_form': form})

def actualizar_insumo(request):
    if request.method == 'POST':
        form = actualizarInsumo(request.POST)
        if form.is_valid():
            id = request.GET.get('id_insumo')
            insumo = Insumos.objects.get(id_venta = id_insumo)
            insumo.insumo = form.cleaned_data['insumo']
            insumo.etapa = form.cleaned_data['etapa']
            isumo.estado = form.cleaned_data['estado']
            insumo.save()
            elemento = generar_tablaInsumo()
            contexto = {'tabla': elemento}
            return render(request, 'prueba/tablaInsumo.html',contexto)
            #return render(request,'prueba/actualizar.html', {'actualizar_form': form, 'id': id})

    form = actualizarInsumo()
    if request.method == 'GET':
        id = request.GET.get('id_insumo')
        if not id:
            return render(request,'prueba/actualizar_insumo.html', {'actualizarinsumo_form': form})
        else:
            # siempre caemos aqui (por medio del boton)

            return render(request,'prueba/actualizar_insumo.html', {'actualizarinsumo_form': form, 'id': id})
    else:
        return render(request,'prueba/actualizar_insumo.html', {'actualizarinsumo_form': form})

#Insercion

def InsertarCarro(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = insertarCarro(request.POST)
        # verifica que sea valido:

        if form.is_valid():
            #id1 = form.cleaned_data['id']
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(id_carro) AS ind FROM public.carro")
                indice = namedtuplefetchall(cursor)
            id1 = indice[0].ind + 1
            producto1 = form.cleaned_data['producto']
            stock1 = form.cleaned_data['stock']
            estado1 = form.cleaned_data['estado']

            elemento = True
            data = Carro(id_carro=id1,producto= producto1, stock= stock1, estado= estado1)
            data.save()
            return render(request, 'prueba/insertarCarro.html', {'carro_form': form,'tabla':elemento,'id': id1,'producto':producto1,'stock':stock1,'estado':estado1})
    # si es GET (o algo diferente) crearemos un formulario en blanco
    else:
        form = insertarCarro()
    return render(request, 'prueba/insertarCarro.html', {'carro_form': form})


def InsertarCliente(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = insertarCliente(request.POST)
        # verifica que sea valido:

        if form.is_valid():
            #id1 = form.cleaned_data['id']
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(id_venta) AS ind FROM public.cliente")
                indice = namedtuplefetchall(cursor)
            id1 = indice[0].ind + 1
            nombre1 = form.cleaned_data['nombre']
            telefono1 = form.cleaned_data['telefono']
            fecha1 = form.cleaned_data['fecha']
            cantidad1 = form.cleaned_data['cantidad']
            precio1 = form.cleaned_data['precio']

            elemento = True
            data = Cliente(id_venta=id1,nombre_cliente= nombre1, telefono= telefono1, fecha= fecha1, cantidad = cantidad1, precio = precio1)
            data.save()
            return render(request, 'prueba/insertarCliente.html', {'inscliente_form': form,'tabla':elemento,'id': id1,'nombre_cliente':nombre1,'telefono':telefono1,'fecha':fecha1, 'cantidad':cantidad1,'precio':precio1})
    # si es GET (o algo diferente) crearemos un formulario en blanco
    else:
        form = insertarCliente()
    return render(request, 'prueba/insertarCliente.html', {'inscliente_form': form})

def InsertarProveedor(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = insertarProveedor(request.POST)
        # verifica que sea valido:

        if form.is_valid():
            #id1 = form.cleaned_data['id']
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(id_compra) AS ind FROM public.proveedor")
                indice = namedtuplefetchall(cursor)
            id1 = indice[0].ind + 1
            empresa1 = form.cleaned_data['empresa']
            telefono1 = form.cleaned_data['telefono']
            fecha1 = form.cleaned_data['fecha']
            cantidad1 = form.cleaned_data['cantidad']
            precio1 = form.cleaned_data['precio']
            insumo1 = form.cleaned_data['insumo']

            elemento = True
            data = Proveedor(id_compra=id1,empresa= empresa1, telefono= telefono1, fecha= fecha1, cantidad = cantidad1, precio = precio1, insumo = insumo1)
            data.save()
            return render(request, 'prueba/insertarProveedor.html', {'insproveedor_form': form,'tabla':elemento,'id': id1,'empresa':empresa1,'telefono':telefono1,'fecha':fecha1, 'cantidad':cantidad1,'precio':precio1,'insumo':insumo1})
    # si es GET (o algo diferente) crearemos un formulario en blanco
    else:
        form = insertarProveedor()
    return render(request, 'prueba/insertarProveedor.html', {'insproveedor_form': form})

def InsertarInsumo(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = insertarInsumo(request.POST)
        # verifica que sea valido:

        if form.is_valid():
            #id1 = form.cleaned_data['id']
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(id_insumo) AS ind FROM public.insumos")
                indice = namedtuplefetchall(cursor)
            id1 = indice[0].ind + 1
            insumo1 = form.cleaned_data['insumoA']
            etapa1 = form.cleaned_data['etapa']
            estado1 = form.cleaned_data['estado']

            elemento = True
            data = Insumos(id_insumo=id1,insumo=insumo1,etapa= etapa1,estado= estado1)
            data.save()
            return render(request, 'prueba/insertarInsumo.html', {'ingresarInsumo_form': form,'tabla':elemento,'id': id1,'insumoAgregado':insumo1,'etapaAgregado':etapa1,'estadoAgregado':estado1})
    # si es GET (o algo diferente) crearemos un formulario en blanco
    else:
        form = insertarInsumo()
    return render(request, 'prueba/insertarInsumo.html', {'ingresarInsumo_form': form})

#Consultas directas
def mayo (request):
    return HttpResponse("El numero del mes 'Mayo' es "+str(Mes.objects.filter(nombre='Mayo')[:1].get().numero))

def mayosql(request):
    return HttpResponse("El numero del mes 'Mayo' es "+ str(consultar_mes('Mayo')[0].numero))

#Formularios para consultas
def consulta11(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = consulta11Form(request.POST)
        # verifica que sea valido:

        if form.is_valid():
            fecha1 = form.cleaned_data['fecha1']
            fecha2 = form.cleaned_data['fecha2']
            elemento = generar_consulta11(fecha1,fecha2)
            #contexto = {'tabla': elemento}

            return render(request, 'prueba/consulta11.html', {'consulta11_form': form, 'tabla':elemento})
    # si es GET (o algo diferente) crearemos un formulario en blanco
    else:
        form = consulta11Form()
    return render(request, 'prueba/consulta11.html', {'consulta11_form': form})

def consulta22(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = consulta22Form(request.POST)
        # verifica que sea valido:

        if form.is_valid():
            hora1 = form.cleaned_data['hora1']
            hora2 = form.cleaned_data['hora2']
            etapa = form.cleaned_data['etapa']
            elemento = generar_consulta22(hora1,hora2,etapa)
            return render(request, 'prueba/consulta22.html', {'consulta22_form': form, 'tabla':elemento})
    # si es GET (o algo diferente) crearemos un formulario en blanco
    else:
        form = consulta22Form()
    return render(request, 'prueba/consulta22.html', {'consulta22_form': form})

def consulta33(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = consulta33Form(request.POST)
        # verifica que sea valido:
        if form.is_valid():
            estado = form.cleaned_data['estado']
            etapa = form.cleaned_data['etapa']
            elemento = generar_consulta33(estado,etapa)
            return render(request, 'prueba/consulta33.html', {'consulta33_form': form, 'tabla':elemento})
    # si es GET (o algo diferente) crearemos un formulario en blanco
    else:
        form = consulta33Form()
    return render(request, 'prueba/consulta33.html', {'consulta33_form': form})

def consulta1(request):
    elemento = generar_consulta1()
    contexto = {'tabla': elemento}
    return render(request, 'prueba/consulta1.html',contexto)

def consulta2(request):
    elemento = generar_consulta2()
    contexto = {'tabla': elemento}
    return render(request, 'prueba/consulta2.html',contexto)

def consulta3(request):
    elemento = generar_consulta3()
    contexto = {'tabla': elemento}
    return render(request, 'prueba/consulta3.html',contexto)

def insumo(request):
    # si es POST, tenemos una peticionn del usuario
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NombreInsumoForm(request.POST)
        # verifica que sea valido:
        if form.is_valid():
            nombre_insumo = form.cleaned_data['nombre_insumo']
            sql_res = consultar_insumo(nombre_insumo)
            if sql_res:
                cant_insumo = consultar_insumo(nombre_insumo)[0].cuenta
                res = 'La cantidad del insumo '+nombre_insumo+' es '+str(cant_insumo)
            else:
                res = 'El insumo '+nombre_insumo+' no esta en la tabla'
            return render(request, 'prueba/insumos.html', {'insumo_form': form, 'resultados': res})
    # si es GET (o algo diferente) crearemos un formulario en blanco
    else:
        form = NombreInsumoForm()
    return render(request, 'prueba/insumos.html', {'insumo_form': form})

#Tablas brutas

def tablaCarro(request):
    elemento = generar_tablaCarro()
    contexto = {'tabla': elemento}
    return render(request, 'prueba/tablaCarro.html',contexto)

def tablaInsumo(request):
    elemento = generar_tablaInsumo()
    contexto = {'tabla': elemento}
    return render(request, 'prueba/tablaInsumo.html',contexto)

def tablaCliente(request):
    elemento = generar_tablaCliente()
    contexto = {'tabla': elemento}
    return render(request, 'prueba/tablaCliente.html',contexto)

def tablaProceso(request):
    elemento = generar_tablaProceso()
    contexto = {'tabla': elemento}
    return render(request, 'prueba/tablaProceso.html',contexto)

def tablaProveedor(request):
    elemento = generar_tablaProveedor()
    contexto = {'tabla': elemento}
    return render(request, 'prueba/tablaProveedor.html',contexto)


#Consultas a las tablas
def generar_tablaCarro():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM public.carro ORDER BY id_carro ASC")
        results = namedtuplefetchall(cursor)
    return results

def generar_tablaInsumo():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM public.insumos ORDER BY id_insumo ASC")
        results = namedtuplefetchall(cursor)
    return results

def generar_tablaCliente():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM public.cliente ORDER BY id_venta ASC")
        results = namedtuplefetchall(cursor)
    return results

def generar_tablaProceso():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM public.proceso ORDER BY id_carro ASC")
        results = namedtuplefetchall(cursor)
    return results

def generar_tablaProveedor():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM public.proveedor ORDER BY id_compra ASC")
        results = namedtuplefetchall(cursor)
    return results

#Consultas con SQL
def generar_consulta1():
    with connection.cursor() as cursor:
        cursor.execute("SELECT insumo, date_part('month',fecha) AS mes, COUNT(insumo) AS cantidad FROM public.proveedor GROUP BY insumo, mes ORDER BY mes")
        results = namedtuplefetchall(cursor)
    return results

def generar_consulta11(f1,f2):
    with connection.cursor() as cursor:
        cursor.execute("SELECT insumo, date_part('month',fecha) AS mes, COUNT(insumo) AS cantidad FROM public.proveedor WHERE fecha BETWEEN %s AND %s GROUP BY insumo, mes ORDER BY mes",[f1,f2])
        results = namedtuplefetchall(cursor)
    return results

def generar_consulta2():
    with connection.cursor() as cursor:
        cursor.execute("SELECT producto, stock, etapa FROM carro NATURAL JOIN proceso WHERE date_part('hour',hora_ingreso)=12 AND etapa LIKE 'secado%'")
        results = namedtuplefetchall(cursor)
    return results

def generar_consulta22(ingreso, salida,etapa):
    etapa += '%'
    with connection.cursor() as cursor:
        cursor.execute("SELECT producto, stock, etapa FROM carro NATURAL JOIN proceso WHERE hora_ingreso >= %s AND hora_salida <= %s AND proceso.etapa LIKE %s",[ingreso,salida,etapa])
        results = namedtuplefetchall(cursor)
    return results

def generar_consulta3():
    with connection.cursor() as cursor:
        cursor.execute("SELECT DISTINCT producto, a.etapa AS etapa, insumo FROM (SELECT producto, etapa FROM carro NATURAL JOIN proceso WHERE estado = 'podrido' AND etapa LIKE 'secado%') AS a, insumos WHERE a.etapa = insumos.etapa")
        results = namedtuplefetchall(cursor)
    return results

def generar_consulta33(estado,etapa):
    etapa += '%'
    with connection.cursor() as cursor:
        cursor.execute("SELECT DISTINCT producto, a.etapa AS etapa, insumo FROM (SELECT producto, etapa FROM carro NATURAL JOIN proceso WHERE estado = %s AND etapa LIKE %s) AS a, insumos WHERE a.etapa = insumos.etapa",[estado,etapa])
        results = namedtuplefetchall(cursor)
    return results

def consultar_insumo(insumo):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS cuenta FROM public.insumos WHERE insumo = %s GROUP BY insumo", [insumo])
        results = namedtuplefetchall(cursor)
    return results

def consultar_mes(mes):
    with connection.cursor() as cursor:
         cursor.execute("SELECT numero FROM public.mes WHERE nombre = %s", [mes])
         results = namedtuplefetchall(cursor)
    return results

#Varios
def namedtuplefetchall(cursor):
    #"Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


# Create your views here.
