from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Lead


def leads_list(request):
    leads = Lead.objects.all()
    context = {
        'name': "Joe",
        'age': 20,
        'leads': leads,
    }
    return render(request, "leads/lead_list.html", context)


def lead_detail(request, pk):
    lead = Lead.objects.get(pk=pk)
    context = {
        "lead": lead,
    }
    return render(request, 'leads/lead_detail.html', context)

def lead_create(request):
    return render(request, 'leads/lead_create.html')