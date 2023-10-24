from django.urls import path

from . import views

app_name = 'quote'

urlpatterns = [
    path('', views.quote, name="Quote")
]