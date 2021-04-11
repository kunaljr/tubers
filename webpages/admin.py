from django.contrib import admin
from .models import Slider,Team,Aboutus
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display=('id','myphoto','first_name','role','created_date')
    list_display_links=('first_name','id')
    search_fields=('first_name','role')
    list_filter=('role',)

class slider(admin.ModelAdmin):
    def sphoto(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))
        

    list_display=('headline','sphoto','button_text')

class aboutus(admin.ModelAdmin):
    def img(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))
    list_display=('id','img','created_date')

admin.site.register(Slider,slider)
admin.site.register(Team,TeamAdmin)
admin.site.register(Aboutus,aboutus)
