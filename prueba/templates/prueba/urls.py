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
    #url(r'^formularioprueba/$',views.pruebaformulario,name='pruebaformulario'),
]
