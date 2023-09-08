from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contacts.models import Contact


# from .models import Listing
# from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# from .choices import state_choices,bedroom_choices,price_choices

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        contex={
            "values":request.POST
        }
        
        if request.method == 'POST':
            username= request.POST['username']
            password= request.POST['password']
            user= auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                messages.success(request, 'You have successfully loged in')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid Credentials')
                return render(request,'accounts/login.html',contex)

        else:
            return render(request,'accounts/login.html',contex)

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        contex={
            "values":request.POST
        }
        if request.method == 'POST':
            first_name= request.POST['first_name']
            last_name= request.POST['last_name']
            username= request.POST['username']
            email= request.POST['email']
            password= request.POST['password']
            password2= request.POST['password2']

            if password != password2:
                messages.error(request, 'Confirm password not match with password')
                return render(request,'accounts/register.html',contex)
            else:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username is taken')
                    return render(request,'accounts/register.html',contex)
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'Email is alrady exists')
                        return render(request,'accounts/register.html',contex)
                    else:
                        user=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password2)
                        user.save()
                        # auth.login(user)
                        messages.success(request,'You are registered now you can log in')
                        return redirect('login')
        else:
            return render(request,'accounts/register.html',contex)


def dashboard(request):
    if request.user.is_authenticated:
        contact_list= Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
        contex={
            "contacts":contact_list
        }

        return render(request,'accounts/dashboard.html',contex)
    else:
        messages.error(request, 'You are not loged in')
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now loged out')
        return redirect('index')

# def search(request):
#     query_listing= Listing.objects.order_by('-list_date').filter(is_published=True)
    
#     if 'keywords' in request.GET:
#         keywords=request.GET['keywords']
#         if keywords:
#             query_listing=query_listing.filter(title__icontains=keywords)
#     if 'city' in request.GET:
#         city=request.GET['city']
#         if city:
#             query_listing=query_listing.filter(city__icontains=city)
#     if 'bedroom' in request.GET:
#         bedroom=request.GET['bedroom']
#         if bedroom:
#             query_listing=query_listing.filter(bedrooms__lte=bedroom)
#     if 'state' in request.GET:
#         bedroom=request.GET['state']
#         if bedroom:
#             query_listing=query_listing.filter(state__iexact=bedroom)
#     if 'price' in request.GET:
#         price=request.GET['price']
#         if price:
#             query_listing=query_listing.filter(price__lte=price)




#     contex={
#         "state_choices":state_choices,
#         "bedroom_choices":bedroom_choices,
#         "price_choices":price_choices,
#         "listings":query_listing,
#         "values":request.GET

#     }
#     return render(request,'listings/search.html',contex)