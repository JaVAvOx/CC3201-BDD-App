from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'mayosql/$', views.mayosql, name = 'mayosql'),
    url(r'^mayo/', views.mayo, name='mayo'),
    url(r'^insumo/$', views.insumo, name='insumo'),
    url(r'^tablaprueba/$', views.tablaprueba, name='tablaprueba'),
   # url(r'^test_insercion/$', views.testinsert, name='test_insercion')
    url(r'^consulta1/$', views.consulta1, name='consulta1'),
    url(r'^consulta2/$', views.consulta2, name='consulta2'),
    url(r'^consulta3/$', views.consulta3, name='consulta3'),
    url(r'^consulta11/$',views.consulta11,name='consulta11'),
    url(r'^consulta22/$',views.consulta22,name='consulta22'),
    url(r'^consulta33/$',views.consulta33,name='consulta33'),
    url(r'^pruebaformulario/$',views.pruebaformulario,name='pruebaformulario'),
    url(r'^tablaCarro/$',views.tablaCarro,name='tablaCarro'),
    url(r'^tablaInsumo/$',views.tablaInsumo,name='tablaInsumo'),
    url(r'^tablaCliente/$',views.tablaCliente,name='tablaCliente'),
    url(r'^tablaProceso/$',views.tablaProceso,name='tablaProceso'),
    url(r'^tablaProveedor/$',views.tablaProveedor,name='tablaProveedor'),
    url(r'^insertarCarro/$',views.InsertarCarro,name='insertarCarro'),
    url(r'^insertarInsumo/$',views.InsertarInsumo,name='insertarInsumo'),
    url(r'^insertarCliente/$',views.InsertarCliente,name='insertarCliente'),
    url(r'^insertarProveedor/$',views.InsertarProveedor,name='insertarProveedor'),
    url(r'^actualizar_proceso/$',views.actualizar_proceso,name='actualizar_proceso'),
    url(r'^actualizar_carro/$',views.actualizar_carro,name='actualizar_carro'),
    url(r'^actualizar_proveedor/$',views.actualizar_proveedor,name='actualizar_proveedor'),
    url(r'^actualizar_insumo/$',views.actualizar_insumo,name='actualizar_insumo'),
    url(r'^actualizar_cliente/$',views.actualizar_cliente,name='actualizar_cliente'),
    #url(r'^actualizar/(?P<author>[-\w]+)/(?P<video>\w+)/(?P<related>\w+)/$', 'video_player'),
    #url(r'^actualizar/$', actualizar),

]
