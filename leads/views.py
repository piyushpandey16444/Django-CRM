from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm
from django.views.generic import ListView, TemplateView, DetailView, CreateView


class LandingPageView(TemplateView):
    template_name = "leads/landing.html"


def landing_page(request):
    return render(request, 'leads/landing.html')


class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


def leads_list(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads,
    }
    return render(request, "leads/lead_list.html", context)


class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


def lead_detail(request, pk):
    lead = Lead.objects.get(pk=pk)
    context = {"lead": lead}
    return render(request, 'leads/lead_detail.html', context)


class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    context_object_name = "lead"

    def get_success_url(self):
        return reverse("leads:lead-list")


def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context = {"form": form}
    return render(request, 'leads/lead_create.html', context)


def lead_update(request, pk):
    lead = Lead.objects.get(pk=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(data=request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')

    context = {"form": form, "lead": lead}
    return render(request, "leads/lead_update.html", context)


def lead_delete(request, pk):
    lead = Lead.objects.get(pk=pk)
    lead.delete()
    return redirect("/leads")
