from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Lead, Agent
from .forms import LeadForm


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
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(data=request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name', False)
            last_name = form.cleaned_data.get('last_name', False)
            age = form.cleaned_data.get('age', False)
            agent = Agent.objects.first()
    context = {"form": form}
    return render(request, 'leads/lead_create.html', context)
