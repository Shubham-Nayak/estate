from django.contrib import admin
from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display=('id','title','price','is_published','list_date','realtor','state')
    list_display_links=('id','title')
    list_filter=('realtor',)
    list_editable=('is_published','price')
    search_fields=('title','state','city','state','price','zipcode')
    list_per_page=20
admin.site.register(Listing,ListingAdmin)