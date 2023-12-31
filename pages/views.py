from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choices,bedroom_choices,price_choices
from django.conf import settings
from settings.models import Setting

# Create your views here.


def index(request):
    settings=Setting.objects.get()
    listings= Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    contex={
        "listings":listings,
        "state_choices":state_choices,
        "bedroom_choices":bedroom_choices,
        "price_choices":price_choices,
        "settings":settings

    }
    return render(request,'pages/index.html',contex)

def about(request):
    settings=Setting.objects.all()
    realtors= Realtor.objects.order_by('-hire_date')
    mvp_reators= Realtor.objects.all().filter(is_mvp=True)
    contex={
        "realtors":realtors,
        "mvp_reators":mvp_reators,
        "settings":settings

    }
    return render(request,'pages/about.html',contex)