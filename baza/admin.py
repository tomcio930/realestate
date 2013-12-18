from django.contrib import admin
from baza.models import Apartment, Address, Locator, Room
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from nested_inlines.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline



class LocatorAdmin(NestedModelAdmin):
    list_display = ('name', 'surname')
    search_fields = ('name', 'surname')
    list_filter = ('name', 'surname',)

class LocatorInline(NestedStackedInline):
    model = Locator
    extra = 0
    
class RoomAdmin(NestedModelAdmin):
    inlines = [LocatorInline, ]
    list_display = ('apartment', 'description', 'is_free', 'rent_time', 'rent_agreement_scan')
    search_fields = ('apartment__address__city', 'apartment__address__street', 'description')
    list_filter = ('apartment', 'is_free', 'rent_time')
 
class RoomInline(NestedStackedInline):
    model = Room
    inlines = [LocatorInline, ]
    extra = 0

class AddressAdmin(NestedModelAdmin):
    list_display = ('city', 'street', 'post_code')
    search_fields = ('city', 'street', 'post_code')
    list_filter = ('city', 'street', 'post_code', )  
    
class ApartmentAdmin(NestedModelAdmin):
    inlines = [RoomInline, ]
    #raw_id_fields = ("address",)
    fieldsets = (
                 (None, {
                         'fields':('address', 'area', 'rent_price', ('can_rent_all_apartment', 'is_free'), 'rent_time')
                }),
                 (_('description'), {
                     'classes': ('collapse',),
                     'fields': ('description', 'notes')       
                }),
    )
    list_display = ('address', 'area', 'rent_price', 'is_free', 'can_rent_all_apartment', 'rent_time')
    search_fields = ('address__city', 'address__street', 'area', 'rent_price', 'is_free')
    list_filter = ('address', 'area', 'rent_price', 'is_free', 'can_rent_all_apartment', 'rent_time')


admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Locator, LocatorAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.unregister(Site)
#admin.site.unregister(User)
#admin.site.unregister(Group)