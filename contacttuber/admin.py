from django.contrib import admin
from .models import Contacttubers
# Register your models here.

class contacttubers(admin.ModelAdmin):
    list_display=('id','full_name','email','phone','subject')

admin.site.register(Contacttubers,contacttubers)
