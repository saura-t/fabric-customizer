from django.shortcuts import render

# Create your views here.
def quote(request, template_name = 'Quote.html'):
    return render(request, template_name)