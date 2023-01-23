from . import models 
from django.contrib import admin

@admin.register (models.User)
class AdminUser (admin.ModelAdmin):
    
    change_form_template = 'admin/change_form_users.html'
    
    list_display = ('id', 'user_name', 'is_active', 'is_admin', 'first_name', 'last_name', 'email', 'phone', 'week_points', 'total_points')
    list_filter = ('country', 'time_zone', 'is_active', 'is_admin')
    ordering = ('id', 'user_name', 'first_name', 'last_name', 'week_points', 'total_points', 'email', 'phone')
    search_fields = ('id', 'user_name', 'first_name', 'last_name', 'email', 'phone', 'country', 'time_zone')
    search_help_text = "Buscar usuarios por nombre, apellido, email, país o zona horaria"

@admin.register (models.Country)
class AdminCountry (admin.ModelAdmin):
    
    list_display = ('id', 'country')
    ordering = ('id', 'country')
    search_fields = ('country', )
    
@admin.register (models.TimeZone)
class AdminTimeZone (admin.ModelAdmin):
    list_display = ('id', 'time_zone')
    ordering = ('id', 'time_zone')
    search_fields = ('time_zone', )
    
@admin.register (models.Stream)
class AdminStream (admin.ModelAdmin):
    
    list_display = ('id', 'user', 'datetime')
    ordering = ('id', 'user', 'datetime')
    list_filter = ('user', 'datetime')
    search_fields = ('user', )
    
@admin.register (models.Comment)
class AdminComment (admin.ModelAdmin):
    
    list_display = ('id', 'user', 'stream', 'comment', 'datetime', 'status')
    ordering = ('id', 'user', 'stream', 'datetime', 'datetime', 'status')
    list_filter = ('user', 'datetime', 'status')
    search_fields = ('user', 'stream', 'comment')
    
@admin.register (models.WhatchCheck)
class AdminWhatchCheck (admin.ModelAdmin):
    
    list_display = ('id', 'user', 'stream', 'datetime', 'status')
    ordering = ('id', 'user', 'stream', 'datetime', 'status')
    list_filter = ('user', 'datetime', 'status')
    search_fields = ('user', 'stream')
    
@admin.register (models.Status)
class AdminStatus (admin.ModelAdmin):
    
    list_display = ('id', 'name')
    ordering = ('id', 'name')
    search_fields = ('name',)
    
@admin.register (models.Point)
class AdminPoint (admin.ModelAdmin):
    
    list_display = ('id', 'user', 'stream', 'datetime')
    ordering = ('id', 'user', 'stream', 'datetime')
    list_filter = ('user', 'stream', 'datetime')
    search_fields = ('user', 'stream')
    
@admin.register (models.Ranking)
class AdminRanking (admin.ModelAdmin):
    
    list_display = ('id', 'name', 'points')
    ordering = ('id', 'name', 'points')
    search_fields = ('name',)
    