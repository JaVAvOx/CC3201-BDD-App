# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Carro(models.Model):
    id_carro = models.IntegerField(primary_key=True)
    producto = models.TextField(blank=True, null=True)
    stock = models.FloatField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carro'


class Cliente(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    nombre_cliente = models.TextField(blank=True, null=True)
    telefono = models.FloatField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Insumos(models.Model):
    id_insumo = models.IntegerField(primary_key=True)
    insumo = models.TextField(blank=True, null=True)
    etapa = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insumos'


class Mes(models.Model):
    nombre = models.TextField(primary_key=True, )
    numero = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mes'


class Proceso(models.Model):
    id_carro = models.IntegerField(primary_key=True)
    etapa = models.TextField(blank=True, null=True)
    hora_ingreso = models.TimeField(blank=True, null=True)
    hora_salida = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proceso'


class Proveedor(models.Model):
    id_compra = models.IntegerField(primary_key=True)
    empresa = models.TextField(blank=True, null=True)
    telefono = models.FloatField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    insumo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'


