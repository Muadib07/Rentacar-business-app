from django.db import models
from django.shortcuts import reverse
import datetime
from facilities.models import Facility

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_num_of_passangers(value):
    if value > 4:
        raise ValidationError(
            _(f'{value} too many passengers'),
            params={'value': value},
        )


def validate_year_of_production(value):
    current_date = datetime.datetime.now()
    min_year_value = 2000
    if current_date.year < value:
        raise ValidationError(
            _(f'{value}  this year can t be more than {current_date.year}'),
            params={'value': value},
        )

    elif min_year_value > value:
        raise ValidationError(
            _(f'this year can t get any smaller than {min_year_value}'),
            params={'min_year_value': min_year_value},
        )


def grater_than_zero(value):
    if value <= 0:
        raise ValidationError(
            _(f'value must be greater than zero {value}'),
            params={'value': value}
        )


class Cars(models.Model):
    CATEGORIES = (
        ('P', 'Paliwo'),
        ('D', 'Diesel'),
        ('G', 'Gaz'),
        ('E', 'Elektryk'),
        ('H', 'Hybryda'),
    )
    id = models.AutoField(primary_key=True, null=False, blank=False)
    mark = models.CharField(max_length=100, null=False, blank=False)
    model = models.CharField(max_length=100, null=False, blank=False)
    year_of_production = models.PositiveSmallIntegerField(null=False,
                                                          blank=False,
                                                          validators=[validate_year_of_production])
    color = models.CharField(max_length=100, null=False, blank=False)
    type_of_car_engine = models.CharField(max_length=20, choices=CATEGORIES)
    car_engine_power = models.PositiveSmallIntegerField(null=False, blank=False, validators=[grater_than_zero])
    mileage = models.PositiveIntegerField(null=False, blank=False, validators=[grater_than_zero])
    daily_rental_cost = models.PositiveSmallIntegerField(null=False, blank=False, validators=[grater_than_zero])
    note = models.TextField(max_length=500, null=False, blank=False)
    air_conditioner = models.BooleanField(verbose_name="air conditioner",
                                          default=True,
                                          help_text="Check if the car is equipped with air conditioning.")
    num_of_passengers = models.PositiveSmallIntegerField(null=False,
                                                         blank=False,
                                                         validators=[validate_num_of_passangers])
    facility_allocation = models.ForeignKey(Facility,
                                            on_delete=models.SET_NULL,
                                            blank=True,
                                            null=True,)
    car_is_rented = models.BooleanField(default=False, null=False, blank=False)

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __int__(self, sale):
        self.daily_rental_cost = sale

    def __str__(self):
        return self.mark

    def get_url(self):
        return reverse('cars_detail', args=self.id)
