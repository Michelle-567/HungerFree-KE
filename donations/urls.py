
from django.urls import path
from . import views

urlpatterns = [
    path("", views.donate_view, name="donate"),
    path('make/', views.make_donation, name='make_donation'),
    path('list/', views.donation_list, name='donation_list'),
    path("form/", views.donate_form_view, name="donate_form")
]

