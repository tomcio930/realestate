from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
import os, string, random

def get_file_path(instance, filename):
    n = 10
    return os.path.join('files/rent_agreements/', ("".join(random.choice(string.digits) for x in range(n)))+filename)

class Address(models.Model):
    city = models.CharField(_('city'), max_length=40)
    street = models.CharField(_('street'), max_length=200)
    post_code = models.CharField(_('post code'), max_length=6)
    def __unicode__(self):
        return unicode(self.city+" "+self.street)
    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')

class Apartment(models.Model):
    address = models.ForeignKey(Address, verbose_name=_('address'))
    area = models.PositiveSmallIntegerField(_('area [m2]'), blank=True, null=True)
    rent_price = models.PositiveSmallIntegerField(_('rent price [pln]'), blank=True, null=True)
    can_rent_all_apartment = models.BooleanField(_('is whole apartment for rent?'), default = True)
    is_free = models.BooleanField(_('is free?'), default = True)
    rent_time = models.DateField(_('rent duration'), blank=True, null=True)
    description = models.TextField(_('decription'), blank=True, null=True)
    notes = models.TextField(_('notes'), blank=True, null=True)
    def __unicode__(self):
        return unicode(self.address)
    class Meta:
        verbose_name = _('apartment')
        verbose_name_plural = _('apartments')
        
class Room(models.Model):
    apartment = models.ForeignKey(Apartment, verbose_name=_('apartment'))
    description = models.CharField(_('description'), max_length=50, help_text = _("Room description. For example big, small, for 2 persons."))
    is_free = models.BooleanField(_('is free?'), default = True)
    rent_time = models.DateField(_('rent duration'), blank=True, null=True)
    rent_agreement_scan = models.FileField(_('rent agreement scan'), upload_to=get_file_path, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.apartment.address.city+", "+self.apartment.address.street+", "+self.description)
    class Meta:
        verbose_name = _('room')
        verbose_name_plural = _('rooms')
        
class Locator(models.Model):
    room = models.ForeignKey(Room, verbose_name=_('room'))
    address = models.ForeignKey(Address, verbose_name=_('address'))
    name = models.CharField(_('name'), max_length=50)
    surname = models.CharField(_('surname'), max_length=50)
    email = models.EmailField(_('email'), blank=True, null=True)
    phone = models.BigIntegerField(_('phone'), blank=True, null=True)
    def __unicode__(self):
        return unicode(self.surname+" "+self.name)
    class Meta:
        verbose_name = _('locator')
        verbose_name_plural = _('locators')


    

        
        

