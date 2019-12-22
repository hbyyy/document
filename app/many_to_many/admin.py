from django.contrib import admin

# Register your models here.
from many_to_many.models import Topping, Pizza, Writer, Platform, Webtoon


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    pass


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    pass


#
# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Shop)
# class ShopAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Item)
# class ItemAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Shipping)
# class ShippingAdmin(admin.ModelAdmin):
#     pass

@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    pass


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    pass


@admin.register(Webtoon)
class WebtoonAdmin(admin.ModelAdmin):
    pass
