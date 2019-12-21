from django.contrib import admin

# Register your models here.
from many_to_many.models import Topping, Pizza


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    pass


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    pass
