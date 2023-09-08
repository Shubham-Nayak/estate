from django.contrib import admin
from .models import Realtor
# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display=('id','name','email','hire_date','phone','is_mvp')
    list_display_links=('id','name')
    search_fields=('name','phone','email')
    list_editable=('is_mvp',)
    list_per_page=20
admin.site.register(Realtor,RealtorAdmin)