from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Contact
from django.core.mail import send_mail


def index(request):
    if request.method == 'POST':
                listing= request.POST['listing']
                listing_id= request.POST['listing_id']
                name= request.POST['name']
                email= request.POST['email']
                phone= request.POST['phone']
                message= request.POST['message']
                realtor_email= request.POST['realtor_email']
                user_id= request.POST['user_id']

                if request.user.is_authenticated:
                    user_id=request.user.id
                    has_contacted=Contact.objects.all().filter(listing_id=listing_id)
                    if has_contacted:
                        messages.error(request,'You have already made inquiry for this listing')
                        return redirect('/listings/'+listing_id)


                contact =Contact(listing=listing,listing_id=listing_id,name=name,phone=phone,email=email,message=message,user_id=user_id)

                contact.save()

                send_mail(
                "New inquiry for "+listing,
                name+" hav some inquiry for "+listing+" plase reached out on phone number: "+phone,
                email,
                ["shubhamnayak22@gmail.com",realtor_email],
                fail_silently=False,
)
                messages.success(request, 'You request has been submitted ! realtor will get back to you soon !')
                return redirect('/listings/'+listing_id)
                