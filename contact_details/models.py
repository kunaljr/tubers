from django.db import models

# Create your models here.
class Contact_detail(models.Model):
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    fb_link=models.CharField(max_length=255, blank=True )
    insta_link=models.CharField(max_length=255,blank=True)
    tweeter_link=models.CharField(max_length=255,blank=True)
    ytube_link=models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.email
    
