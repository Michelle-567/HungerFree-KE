from django.urls import path
from . import views

urlpatterns = [
    path('', views.partners_view, name='partners'),
]
