from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadModelForm, LeadForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


class LandingPageView(TemplateView):
    template_name = "landing.html"


# def landing_page(request):
#     return render(request, "landing.html")


class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"  # this line of code customizes the context variable and changes default 'object_list' to 'leads'


# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {
#         "leads": leads
#     }
#     return render(request, "leads/lead_list.html", context)


class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"  # this line of code customizes the context variable and changes default 'object_list' to 'lead'


# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         "lead": lead
#     }
#     return render(request, "leads/lead_detail.html", context)


class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


# def lead_create(request):
#     form = LeadModelForm()  # if the request method is not POST, then it should instantiate the empty form
#     print(request.POST)
#     if request.method == "POST":
#         print("Receiving a post request")
#         form = LeadModelForm(
#             request.POST)  # if the request method IS POST, then it should reassign to form with post data being passed into it
#         if form.is_valid():
#             # print("The form is valid")
#             # print(form.cleaned_data)
#             # first_name = form.cleaned_data['first_name']
#             # last_name = form.cleaned_data['last_name']
#             # age = form.cleaned_data['age']
#             # agent = form.cleaned_data['agent']
#             # Lead.objects.create(
#             #     first_name=first_name,
#             #     last_name=last_name,
#             #     age=age,
#             #     agent=agent
#             # )
#             # print("Lead has been created")
#
#             # As we have used LeadModelForm instead of LeadForm
#             # we can avoid above commented boiler-plate code and
#             # use just form.save() method
#             form.save()
#             return redirect("/leads")
#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)


class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == "POST":
#         form = LeadModelForm(
#             request.POST,
#             instance=lead)  # if the request method IS POST, then it should reassign to form with post data being passed into it
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context = {
#         "form": form,
#         "lead": lead
#     }
#     return render(request, "leads/lead_update.html", context)


class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")

# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect("/leads")

# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()  # if the request method is not POST, then it should instantiate the empty form
#     if request.method == "POST":
#         form = LeadForm(request.POST)  # if the request method IS POST, then it should reassign to form with post data being passed into it
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             return redirect("/leads")
#     context = {
#         "form": form,
#         "lead": lead
#     }
#     return render(request, "leads/lead_update.html", context)
