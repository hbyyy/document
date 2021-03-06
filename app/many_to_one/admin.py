from django.contrib import admin

# Register your models here.
from many_to_one.models import Manufacturer, Car


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
