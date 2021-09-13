from django.contrib import admin
from .forms import *
from .models import *


@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    form = ServiceForm


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'email')
    form = ContactForm


@admin.register(DefaultContact)
class DefaultContactAdmin(admin.ModelAdmin):
    list_display = ('number', 'email', 'address')
