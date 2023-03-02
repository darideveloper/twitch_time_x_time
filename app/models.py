import pytz
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User as UserAuth
# from django.contrib.auth import get_user_model

# UserAuth = get_user_model()


class AdminType (models.Model):
    id = models.AutoField(primary_key=True, name='id', verbose_name="id", help_text="id del tipo de administrador", null=False, blank=False, editable=False)
    name = models.CharField(name='name', verbose_name="nombre", help_text="nombre del tipo de administrador", null=False, blank=False, max_length=100)
    ranking = models.ForeignKey('Ranking', on_delete=models.CASCADE, name='ranking', verbose_name="ranking", help_text="ranking asignado al tipo de administrador", null=False, blank=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Tipo de admin"
        verbose_name_plural = "Tipos de admins"

class Ranking (models.Model):
    id = models.AutoField(primary_key=True, name='id', verbose_name="id", help_text="id del ranking", null=False, blank=False, editable=False)
    name = models.CharField(name='name', verbose_name="nombre", help_text="nombre del ranking", null=False, blank=False, max_length=100)
    points = models.IntegerField(name='points', verbose_name="puntos", help_text="puntos requeridos para el ranking", null=False, blank=False)
    max_streams = models.IntegerField(name='max_streams', verbose_name="máximo de streams", help_text="máximo de streams que puede tener el usuario para el ranking", null=False, blank=False, default=0)
    
    @classmethod
    def get_lower(cls):
        return cls.objects.all().order_by('points').first()
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Ranking"
        verbose_name_plural = "Rankings"

class User (models.Model):
    id = models.IntegerField(primary_key=True, name='id', verbose_name="id", help_text="id de twitch", null=False, blank=False, editable=False)
    email = models.EmailField(name='email', verbose_name="email", help_text="email de twitch", null=False, blank=True)
    picture = models.CharField(name='picture', verbose_name="foto", help_text="foto de perfil de twitch", null=False, blank=True, max_length=200)
    user_name = models.CharField(name='user_name', verbose_name="usuario", help_text="nombre de usuario de twitch", null=False, blank=True, max_length=100)
    access_token = models.CharField(name='access_token', verbose_name="access token", help_text="access token generado por twitch", null=False, blank=False, max_length=50)
    refresh_token = models.CharField(name='refresh_token', verbose_name="refresh token", help_text="refresh token generado por twitch", null=False, blank=False, max_length=50)
    last_login = models.DateTimeField(name='last_login', verbose_name="últimos login", help_text="fecha de último inicio de sesión", default=timezone.now)
    first_name = models.CharField(name='first_name', verbose_name="nombre", help_text="nombre real del usuario", null=True, blank=True, max_length=100)
    last_name = models.CharField(name='last_name', verbose_name="apellido", help_text="apellido real del usuario", null=True, blank=True, max_length=100)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, name='country', verbose_name="país", help_text="país de residencia", null=True, blank=True)
    phone = models.CharField(name='phone', verbose_name="teléfono", help_text="teléfono con código de país", null=True, blank=True, max_length=20)
    time_zone = models.ForeignKey('TimeZone', on_delete=models.CASCADE, name='time_zone', verbose_name="zona horaria", help_text="zona horaria", null=True, blank=True)
    is_active = models.BooleanField(name='is_active', verbose_name="activo", help_text="indica si el usuario ha validado su cuenta con whatsapp", default=False)
    ranking = models.ForeignKey('Ranking', on_delete=models.SET_NULL, name='ranking', verbose_name="ranking", help_text="ranking del usuario", null=True, blank=True)
    admin_type = models.ForeignKey('AdminType', on_delete=models.SET_NULL, name='admin_type', verbose_name="tipo de administrador", help_text="tipo de administrador del usuario", null=True, blank=True)
    
    def __str__(self):
        return f"{self.user_name}"
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['user_name']
    
class TimeZone (models.Model):
    id = models.AutoField(primary_key=True, name='id', verbose_name="id", help_text="id de la zona horaria", null=False, blank=False, editable=False)
    time_zone = models.CharField(name='time_zone', verbose_name="zona horaria", help_text="zona horaria", null=False, blank=False, max_length=100)

    def __str__(self):
        return self.time_zone
    
    class Meta:
        verbose_name = "Zona Horaria"
        verbose_name_plural = "Zonas Horarias"

class Country (models.Model):
    id = models.AutoField(primary_key=True, name='id', verbose_name="id", help_text="id del país", null=False, blank=False, editable=False)
    country = models.CharField(name='country', verbose_name="país", help_text="país de residencia", null=False, blank=False, max_length=100)

    def __str__(self):
        return self.country
    
    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"
        
class Stream (models.Model):
    id = models.AutoField(primary_key=True, name='id', verbose_name="id", help_text="id del stream", null=False, blank=False, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, name='user', verbose_name="usuario", help_text="usuario que está transmitiendo", null=False, blank=False)
    datetime = models.DateTimeField(name='datetime', verbose_name="fecha y hora", help_text="fecha y hora del stream", null=False, blank=False, default=timezone.now)
    is_free = models.BooleanField(name='is_free', verbose_name="free", help_text="indica si el stream es free (no restará puntos)", default=False)
    is_vip = models.BooleanField(name='is_vip', verbose_name="vip", help_text="indica si el stream es vip (único en su hora)", default=False)
    
    def __str__(self):
        formated_date = str(timezone.localtime(self.datetime))[0:-12] + "h"
        return f"{self.user.user_name} {formated_date}"
    
    class Meta:
        verbose_name = "Stream"
        verbose_name_plural = "Streams"
        
class Comment (models.Model):
    id = models.AutoField(primary_key=True, name='id', verbose_name="id", help_text="id del comentario", null=False, blank=False, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, name='user', verbose_name="usuario", help_text="usuario que ha hecho el comentario", null=False, blank=False)
    stream = models.ForeignKey('Stream', on_delete=models.CASCADE, name='stream', verbose_name="stream", help_text="stream al que pertenece el comentario", null=False, blank=False)
    datetime = models.DateTimeField(name='datetime', verbose_name="fecha y hora", help_text="fecha y hora del comentario", null=False, blank=False, default=timezone.now)
    comment = models.TextField(name='comment', verbose_name="comentario", help_text="comentario", null=False, blank=False)
    status = models.ForeignKey('Status', on_delete=models.CASCADE, name='status', verbose_name="estado", help_text="estado del check", null=False, blank=False, default=1)
        
    def __str__(self):
        return f"{self.user}: {self.comment} - {self.stream.user.user_name}"
    
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        
class WhatchCheck (models.Model):
    id = models.AutoField(primary_key=True, name='id', verbose_name="id", help_text="id del check", null=False, blank=False, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, name='user', verbose_name="usuario", help_text="usuario que asistió al stream", null=False, blank=False)
    stream = models.ForeignKey('Stream', on_delete=models.CASCADE, name='stream', verbose_name="stream", help_text="stream al que pertenece el check", null=False, blank=False)
    datetime = models.DateTimeField(name='datetime', verbose_name="fecha y hora", help_text="fecha y hora del check", null=False, blank=False, default=timezone.now)
    status = models.ForeignKey('Status', on_delete=models.CASCADE, name='status', verbose_name="estado", help_text="estado del check", null=False, blank=False, default=1)
    
    def __str__(self):
        return f"{self.user}: {self.datetime} - {self.stream.user.user_name}"
    
    class Meta:
        verbose_name = "Check"
        verbose_name_plural = "Checks"
        
class Status (models.Model):
    id = models.AutoField(primary_key=True, name='id', verbose_name="id", help_text="id del estado", null=False, blank=False, editable=False)
    name = models.CharField(name='name', verbose_name="nombre", help_text="nombre del estado", null=False, blank=False, max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Estatus"
        verbose_name_plural = "Estatus"
        
class InfoPoint (models.Model):
    id = models.AutoField(primary_key=True, name='id', verbose_name="id", help_text="id de la información de punto", null=False, blank=False, editable=False)
    info = models.CharField(name='info', verbose_name="información", help_text="información del punto", null=False, blank=False, max_length=100)
    
    def __str__(self):
        return self.info
    
    class Meta:
        verbose_name = "Información de punto"
        verbose_name_plural = "Puntos información"

class GeneralPoint (models.Model):
    id = models.AutoField(primary_key=True, name='id', verbose_name="id", help_text="id del punto", null=False, blank=False, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, name='user', verbose_name="usuario", help_text="usuario que ha hecho el punto", null=False, blank=False)
    stream = models.ForeignKey('Stream', on_delete=models.CASCADE, name='stream', verbose_name="stream", help_text="stream al que pertenece el punto", null=True, blank=True)
    datetime = models.DateTimeField(name='datetime', verbose_name="fecha y hora", help_text="fecha y hora del punto", null=False, blank=False, default=timezone.now)
    amount = models.IntegerField(name='amount', verbose_name="cantidad", help_text="cantidad de puntos", null=False, blank=False, default=1)
    info = models.ForeignKey('InfoPoint', on_delete=models.CASCADE, name='info', verbose_name="información", help_text="información del punto", null=False, blank=False, default=1)
    
    def __str__(self):
        stream_user = ""
        if self.stream:
            stream_user = f"- {self.stream.user.user_name}"
        time_user = timezone.localtime(self.datetime, pytz.timezone(timezone.get_current_timezone_name()))
        return f"{self.user} ({self.amount}): {time_user} {stream_user}"
    
    class Meta:
        verbose_name = "Punto general"
        verbose_name_plural = "Puntos generales"

class WeeklyPoint (models.Model):
    id = models.AutoField(primary_key=True, name='id', verbose_name="id", help_text="id del punto", null=False, blank=False, editable=False)
    general_point = models.ForeignKey('GeneralPoint', on_delete=models.CASCADE, name='general_point', verbose_name="punto general", help_text="punto general al que pertenece el punto", null=False, blank=False)

    def __str__(self):
        return str(self.general_point)
    
    class Meta:
        verbose_name = "Punto semanal"
        verbose_name_plural = "Puntos semanales"
        
class DailyPoint (models.Model):
    id = models.AutoField(primary_key=True, name='id', verbose_name="id", help_text="id del punto", null=False, blank=False, editable=False)
    general_point = models.ForeignKey('GeneralPoint', on_delete=models.CASCADE, name='general_point', verbose_name="punto general", help_text="punto general al que pertenece el punto", null=False, blank=False)

    def __str__(self):
        return str(self.general_point)
    
    class Meta:
        verbose_name = "Punto diarios"
        verbose_name_plural = "Puntos diarios"
        
class Bits (models.Model):
    id = models.AutoField(primary_key=True, name='id', verbose_name="id", help_text="id de los bits", null=False, blank=False, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, name='user', verbose_name="usuario", help_text="usuario que ha hecho el punto", null=False, blank=False)
    amount = models.IntegerField(name='amount', verbose_name="cantidad", help_text="cantidad de bits", null=False, blank=False)
    
    def __str__(self):
        return f"{self.amount} bits ({self.user})"
    
    class Meta:
        verbose_name = "Bit"
        verbose_name_plural = "Bits"

class PointsHistory (models.Model):
    id = models.AutoField(primary_key=True, name='id', verbose_name="id", help_text="id del historial", null=False, blank=False, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, name='user', verbose_name="usuario", help_text="usuario que ha hecho el punto", null=False, blank=False)
    general_points = models.IntegerField(name='general_points', verbose_name="puntos generales", help_text="puntos generales", null=False, blank=False)
    week_points = models.IntegerField(name='week_points', verbose_name="puntos semanales", help_text="puntos semanales", null=False, blank=False)
    
    def __str__(self):
        return f"{self.user} (general: {self.general_points}, semana: {self.week_points})"
    
    class Meta:
        verbose_name = "Historial de puntos generales y semanales"
        verbose_name_plural = "Puntos historial"
        
class TopDailyPoint (models.Model):
    position = models.IntegerField(name='position', verbose_name="posición", help_text="posición del usuario en el top diario", null=False, blank=False, default=10)
    user = models.ForeignKey('User', on_delete=models.CASCADE, name='user', verbose_name="usuario", help_text="usuario que ha hecho conseguido 10 puntos diarios", null=False, blank=False)
    datetime = models.DateTimeField(name='datetime', verbose_name="fecha y hora", help_text="fecha y hora en que el usuario consiguió los 10 puntos diarios", null=False, blank=False, default=timezone.now)
    
    def __str__(self):
        return f"{self.position} {self.user}"
    
    class Meta:
        verbose_name = "Top"
        verbose_name_plural = "Puntos diarios top"
        
class StreamExtra (models.Model):
    id = models.AutoField(primary_key=True, name='id', verbose_name="id", help_text="id del stream extra", null=False, blank=False, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, name='user', verbose_name="usuario", help_text="usuario al que se le ha asignado el stream extra", null=False, blank=False)
    amount = models.IntegerField(name='amount', verbose_name="cantidad", help_text="cantidad de estreams extra", null=False, blank=False, default=1)
    
    def __str__(self):
        return f"({self.amount}) {self.user}"
    
    class Meta:
        verbose_name = "Stream extra"
        verbose_name_plural = "Streams extra"
        
class StreamVip (models.Model):
    id = models.AutoField(primary_key=True, name='id', verbose_name="id", help_text="id del vip extra", null=False, blank=False, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, name='user', verbose_name="usuario", help_text="usuario  al que se le ha asignado el vip", null=False, blank=False)
    amount = models.IntegerField(name='amount', verbose_name="cantidad", help_text="cantidad de vips", null=False, blank=False, default=1)
    
    def __str__(self):
        return f"({self.amount}) {self.user}"
    
    class Meta:
        verbose_name = "Stream Vip"
        verbose_name_plural = "Streams Vip"
        
class UserStaff (models.Model):
    id = models.AutoField(primary_key=True, name='id', verbose_name="id", help_text="id del usuario staff", null=False, blank=False, editable=False)
    user_auth = models.ForeignKey(UserAuth, on_delete=models.CASCADE, name='user_auth', verbose_name="usuario de autenticación", help_text="usuario del dashboard", null=False, blank=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, name='user', verbose_name="usuario", help_text="usuario de twitch", null=False, blank=False)
    
    def __str__(self):
        return f"{self.user_auth.username} - {self.user}"
    
    class Meta:
        verbose_name = "Usuario staff relacion"
        verbose_name_plural = "Usuarios staff relaciones"