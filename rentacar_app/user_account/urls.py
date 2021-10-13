from django.urls import path
from . import views
from django.conf.urls import include


urlpatterns = [
    # path('change_password/', views.password_change_view, name='name_change_password'),
    path('register/', views.register_view, name='register'),
    path('details/', views.register_view, name='details'),
]