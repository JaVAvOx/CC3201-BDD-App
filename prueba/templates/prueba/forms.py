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
		hora1 = forms.CharField(label='Hora ingreso:',max_length=10)
		hora2 = forms.CharField(label='Hora salida:',max_length=10)
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
	id = forms.CharField(label='ID:',max_length=10)
	producto = forms.ChoiceField(choices=[("ciruela", "Ciruela"),("papaya", "Papaya"),("mango", "Mango"),("damasco", "Damasco"),("durazno", "Durazno"),("uva", "Uva")],widget=forms.Select())
	stock = forms.CharField(label='Stock:',max_length=10)
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
