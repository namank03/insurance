from django.contrib import admin

from .models import Customer, Policy

# Register your models here.
admin.site.register(Policy)
admin.site.register(Customer)
