from django.shortcuts import render
from .models import Contact_detail
# Create your views here.
def contact_detail(request):
    contact_detail=Contact_detail.objects.all() 
    data={
        'contact_detail':contact_detail,
    }
    return render(request,'includes/header.html',data)