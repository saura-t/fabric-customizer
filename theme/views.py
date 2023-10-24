from django.shortcuts import render

# Create your views here.
def home(request, template_name='Home.html'):
    return render(request, template_name)