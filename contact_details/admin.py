from django.contrib import admin
from .models import Contact_detail
# Register your models here.

class contact_detail(admin.ModelAdmin):
    list_display=('email','phone','address','fb_link','insta_link','tweeter_link','ytube_link')

admin.site.register(Contact_detail,contact_detail)
