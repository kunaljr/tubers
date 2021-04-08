from django.urls import path
from . import views

urlpatterns=[
    path('contacttubers',views.contacttubers,name="contacttubers"),
]