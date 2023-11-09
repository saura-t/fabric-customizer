from django.shortcuts import render

# Create your views here.
def base(request, template_name='Base.html'):
    return render(request, template_name)