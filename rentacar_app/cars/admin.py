from django.contrib import admin
from .models import Cars


class AdminCarsOverview(admin.ModelAdmin):
    list_display = ('model', 'color', 'air_conditioner', 'year_of_production', 'daily_rental_cost')
    search_fields = ('model', 'category')
    ordering = ('daily_rental_cost',)
    list_filter = ('car_engine_power', 'type_of_car_engine',)


admin.site.register(Cars, AdminCarsOverview)
