from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def quote(request, template_name = 'Quote.html'):
    return render(request, template_name, {})

def costing(request, template_name = 'Costing.html'):
    return render(request, template_name, {})