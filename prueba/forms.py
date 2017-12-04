from django import forms
from django.db import models
from django.forms import ModelForm
#from django.forms.extras.widgets import SelectTimeWidget



class NombreInsumoForm(forms.Form):
	nombre_insumo = forms.CharField(label='Nombre del insumo', max_length=100)

class tablapruebaForm(forms.Form):
        nombre_tabla = forms.CharField(label='tabla', max_length=100)


class consulta11Form(forms.Form):
	fecha1 = forms.DateField(widget = forms.SelectDateWidget())
	fecha2 = forms.DateField(widget = forms.SelectDateWidget())
		#fecha1 = forms.CharField(label='fecha 1:',max_length=10)
		#fecha2 = forms.CharField(label='fecha 2:',max_length=10)

class consulta22Form(forms.Form):
		hora1 = forms.CharField(label='Hora ingreso:',max_length=4)
		hora2 = forms.CharField(label='Hora salida:',max_length=4)
		#hora1 = forms.TimeField(widget = forms.SelectTimeWidget())
		#hora2 = forms.TimeField(widget = forms.SelectTimeWidget())
		etapa = forms.ChoiceField(choices=[("packing", "Packing"),("extraccion", "Extraccion"),("secado horno", "Secado Horno"),("secado cancha", "Secado Cancha"),("precosecha", "Precosecha")],widget=forms.Select())

class consulta33Form(forms.Form):
		estado = forms.ChoiceField(choices=[("bueno", "Bueno"),("podrido", "Podrido"),("maduro", "Maduro"),("inmaduro", "Inmaduro")],widget=forms.Select())
		etapa = forms.ChoiceField(choices=[("packing", "Packing"),("extraccion", "Extraccion"),("secado horno", "Secado Horno"),("secado cancha", "Secado Cancha"),("precosecha", "Precosecha")],widget=forms.Select())

class pruebaForm(forms.Form):
	estado = forms.CharField(label='Estado:',max_length=10)
	etapa = forms.CharField(label='Etapa:',max_length=10)
	reason = forms.ChoiceField(choices=[("feature", "A feature"),("order", "An order")],widget=forms.Select())
	Date = forms.DateField(widget = forms.SelectDateWidget())


class insertarCarro(forms.Form):
	#id = forms.CharField(label='ID:',max_length=10)
	producto = forms.ChoiceField(choices=[("ciruela", "Ciruela"),("papaya", "Papaya"),("mango", "Mango"),("damasco", "Damasco"),("durazno", "Durazno"),("uva", "Uva")],widget=forms.Select())
	stock = forms.CharField(label='Stock:',max_length=10)
	estado = forms.ChoiceField(choices=[("bueno", "Bueno"),("podrido", "Podrido"),("maduro", "Maduro"),("inmaduro", "Inmaduro")],widget=forms.Select())

class actualizarProceso(forms.Form):
                hora_ingreso = forms.CharField(label='Hora ingreso:', max_length=5)
                hora_salida = forms.CharField(label='Hora salida:', max_length=5)
                etapa = forms.ChoiceField(choices=[("packing", "Packing"),("extraccion", "Extraccion"),("secado horno", "Secado Horno"),("secado cancha", "Secado Cancha"),("precosecha", "Precosecha")],widget=forms.Select())


class actualizarCarro(forms.Form):
				producto = forms.ChoiceField(choices=[("ciruela", "Ciruela"),("papaya", "Papaya"),("mango", "Mango"),("damasco", "Damasco"),("durazno", "Durazno"),("uva", "Uva")],widget=forms.Select())
				stock = forms.CharField(label='Stock:',max_length=10)
				estado = forms.ChoiceField(choices=[("bueno", "Bueno"),("podrido", "Podrido"),("maduro", "Maduro"),("inmaduro", "Inmaduro")],widget=forms.Select())

class actualizarInsumo(forms.Form):
	#id = forms.CharField(label='ID:',max_length=10)
	insumo = forms.CharField(label='Insumo:',max_length=20)
	etapa = forms.ChoiceField(choices=[("packing", "Packing"),("extraccion", "Extraccion"),("secado horno", "Secado Horno"),("secado cancha", "Secado Cancha"),("precosecha", "Precosecha")],widget=forms.Select())
	estado = forms.ChoiceField(choices=[("bueno", "Bueno"),("podrido", "Podrido"),("maduro", "Maduro"),("inmaduro", "Inmaduro")],widget=forms.Select())

class actualizarProveedor(forms.Form):
	#id = forms.CharField(label='ID:',max_length=10)
	empresa = forms.ChoiceField(choices=[("COMERCIAL CARLOS HIDALGO","COMERCIAL CARLOS HIDALGO"),("FUNDO CASIMIRO","FUNDO CASIMIRO"),("FUNDO PABLO NERUDA","FUNDO PABLO NERUDA"),("LO VALLEDOR", "LO VALLEDOR")], widget = forms.Select())
	telefono = forms.ChoiceField(choices=[("56965873284","56965873284"),("56946825374","56946825374"),("56984675826","56984675826"),("56978456285","56978456285")],widget=forms.Select())
	fecha = forms.DateField(widget = forms.SelectDateWidget())
	cantidad = forms.CharField(label='Cantidad:',max_length=10)
	precio = forms.CharField(label='Precio:',max_length=15)
	insumo = forms.CharField(label='Insumo:',max_length=20)

class actualizarCliente(forms.Form):
	#id = forms.CharField(label='ID:',max_length=10)
	nombre = forms.ChoiceField(choices=[("COPEFRUT S.A.","COPEFRUT S.A."),("EL MAIPO","EL MAIPO"),("EXPORTADORA SANTA CRUZ S.A","EXPORTADORA SANTA CRUZ S.A"),("RUCARAY S.A", "RUCARAY S.A"),("SOCIEDAD AGRICOLA EXPORTADORA VERFRUT S.A.","SOCIEDAD AGRICOLA EXPORTADORA VERFRUT S.A.")], widget = forms.Select())
	telefono = forms.ChoiceField(choices=[("56978424615","56978424615"),("56983125165","56983125165"),("56945782168","56945782168"),("56979815136","56979815136"),("56945678124","56945678124")],widget=forms.Select())
	fecha = forms.DateField(widget = forms.SelectDateWidget())
	cantidad = forms.CharField(label='Cantidad:',max_length=10)
	precio = forms.CharField(label='Precio:',max_length=15)


class insertarProveedor(forms.Form):
	empresa = forms.ChoiceField(choices=[("COMERCIAL CARLOS HIDALGO","COMERCIAL CARLOS HIDALGO"),("FUNDO CASIMIRO","FUNDO CASIMIRO"),("FUNDO PABLO NERUDA","FUNDO PABLO NERUDA"),("LO VALLEDOR", "LO VALLEDOR")], widget = forms.Select())
	telefono = forms.ChoiceField(choices=[("56965873284","56965873284"),("56946825374","56946825374"),("56984675826","56984675826"),("56978456285","56978456285")],widget=forms.Select())
	fecha = forms.DateField(widget = forms.SelectDateWidget())
	cantidad = forms.CharField(label='Cantidad:',max_length=10)
	precio = forms.CharField(label='Precio:',max_length=15)
	insumo = forms.CharField(label='Insumo:',max_length=20)

class insertarCliente(forms.Form):
	nombre = forms.ChoiceField(choices=[("COPEFRUT S.A.","COPEFRUT S.A."),("EL MAIPO","EL MAIPO"),("EXPORTADORA SANTA CRUZ S.A","EXPORTADORA SANTA CRUZ S.A"),("RUCARAY S.A", "RUCARAY S.A"),("SOCIEDAD AGRICOLA EXPORTADORA VERFRUT S.A.","SOCIEDAD AGRICOLA EXPORTADORA VERFRUT S.A.")], widget = forms.Select())
	telefono = forms.ChoiceField(choices=[("56978424615","56978424615"),("56983125165","56983125165"),("56945782168","56945782168"),("56979815136","56979815136"),("56945678124","56945678124")],widget=forms.Select())
	fecha = forms.DateField(widget = forms.SelectDateWidget())
	cantidad = forms.CharField(label='Cantidad:',max_length=10)
	precio = forms.CharField(label='Precio:',max_length=15)

class insertarInsumo(forms.Form):
	#id = forms.CharField(label='ID:',max_length=10)
	insumoA = forms.CharField(label='Insumo:',max_length=20)
	etapa = forms.ChoiceField(choices=[("packing", "Packing"),("extraccion", "Extraccion"),("secado horno", "Secado Horno"),("secado cancha", "Secado Cancha"),("precosecha", "Precosecha")],widget=forms.Select())
	estado = forms.ChoiceField(choices=[("bueno", "Bueno"),("podrido", "Podrido"),("maduro", "Maduro"),("inmaduro", "Inmaduro")],widget=forms.Select())



#para la consulta3 preguntamos el estado del producto
"""
class estadoproductoForm(forms.Form):
        estado_producto = froms.CharField(label='Estado del producto', max_length=100)


class TestInsercion(models.Model):
        id = models.IntegerField(label = 'ID')
        nom = models.CharField(label = 'nombre', max_length=30)
        app = models.CharField(label = 'apellido', max_length = 30)
        cap = models.IntegerField(label = 'capital')

        def __str__(self):
                return self.name


class TestInsercionForm(ModelForm):
        class Meta:
                model = TestInsercion
                fields = ['id','nom','app','cap']

"""


class DateInput(forms.DateInput):
    input_type = 'date'
