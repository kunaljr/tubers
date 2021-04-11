from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Slider, Team, Aboutus
from youtubers.models import Youtuber
from contact_details.models import Contact_detail
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import razorpay
# Create your views here.

def home(request):
    contact_detail=Contact_detail.objects.all() 
    sliders=Slider.objects.all()
    teams=Team.objects.all()
    featured_youtubers=Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_tubers=Youtuber.objects.order_by('-created_date')
    data = {
        'sliders': sliders,
        'teams':teams ,
        'featured_youtubers':featured_youtubers,
        'all_tubers':all_tubers,
        'contact_detail':contact_detail
    }
    return render(request,'webpages/home.html',data)

def about(request):
    contact_detail=Contact_detail.objects.all() 
    teams=Team.objects.all()
    aboutus=Aboutus.objects.order_by('-created_date')
    data={
        'teams':teams,
        'aboutus':aboutus,
        'contact_detail':contact_detail
    }
    return render(request,'webpages/about.html',data)

def services(request):
    contact_detail=Contact_detail.objects.all()
    tubers=Youtuber.objects.order_by('-created_date')
    city_search=Youtuber.objects.values_list('city',flat=True)
    camera_type_search=Youtuber.objects.values_list('camera_type',flat=True)
    category_search=Youtuber.objects.values_list('category',flat=True)
    if request.method == 'POST':
        amount = 50000
        order_currency = 'INR'
        client= razorpay.Client(auth=('rzp_test_31strWsI9bxav2','mM5xQlqkxPoslSEvL1dEiM98'))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        messages.success(request,'Thank You for a Coffee')
        return redirect('services')

    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            tubers= tubers.filter(city__iexact=city)

    if 'camera_type' in request.GET:
        camera_type=request.GET['camera_type']
        if camera_type:
            tubers= tubers.filter(camera_type__iexact=camera_type)

    if 'category' in request.GET:
        category=request.GET['category']
        if category:
            tubers= tubers.filter(category__iexact=category)

    data={
        'tubers':tubers,
        'city_search':city_search,
        'camera_type_search':camera_type_search,
        'category_search':category_search,
        'contact_detail':contact_detail,
        
    }
    return render(request,'webpages/services.html',data)

def contact(request):
    contact_detail=Contact_detail.objects.all()
    data={
        
        'contact_detail':contact_detail
    }
    return render(request,'webpages/contact.html',data)

@csrf_exempt
def success(request):
    return render(request,'webpages/success.html')
