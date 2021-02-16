from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead


def home_view(request):
    leads = Lead.objects.all()
    context = {
        'name': "Joe",
        'age': 20,
        'leads': leads,
    }
    return render(request, "leads/home_page.html", context)
