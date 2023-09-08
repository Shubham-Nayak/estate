from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .choices import state_choices,bedroom_choices,price_choices

# Create your views here.


def index(request):
    listings= Listing.objects.order_by('-list_date').filter(is_published=True)
   

    paginator= Paginator(listings,3)
    page= request.GET.get('page')
    paged_listings= paginator.get_page(page)
    contex={
        "listings":paged_listings
    }
    return render(request,'listings/listings.html',contex)

def listing(request,listing_id):
    listing= get_object_or_404(Listing,pk=listing_id)
    contex={ 
        "listing":listing
    }
    return render(request,'listings/listing.html',contex)

def search(request):
    query_listing= Listing.objects.order_by('-list_date').filter(is_published=True)
    
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            query_listing=query_listing.filter(title__icontains=keywords)
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            query_listing=query_listing.filter(city__icontains=city)
    if 'bedroom' in request.GET:
        bedroom=request.GET['bedroom']
        if bedroom:
            query_listing=query_listing.filter(bedrooms__lte=bedroom)
    if 'state' in request.GET:
        bedroom=request.GET['state']
        if bedroom:
            query_listing=query_listing.filter(state__iexact=bedroom)
    if 'price' in request.GET:
        price=request.GET['price']
        if price:
            query_listing=query_listing.filter(price__lte=price)




    contex={
        "state_choices":state_choices,
        "bedroom_choices":bedroom_choices,
        "price_choices":price_choices,
        "listings":query_listing,
        "values":request.GET

    }
    return render(request,'listings/search.html',contex)