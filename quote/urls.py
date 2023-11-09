from django.urls import path

from . import views

app_name = 'quote'

urlpatterns = [
    path('newQuote/', views.quote, name="Quote"),
    path('costing/', views.costing, name="Costing"),
]
