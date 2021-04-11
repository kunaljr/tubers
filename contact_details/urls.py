from django.urls import path
from . import views

urlpatterns=[
    path('contact_detail',views.contact_detail,name="contact_detail")
]