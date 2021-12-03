from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadModelForm


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)


def lead_create(request):
    form = LeadModelForm() #if the request method is not POST, then it should instantiate the empty form
    print(request.POST)
    if request.method == "POST":
        print("Receiving a post request")
        form = LeadModelForm(request.POST) #if the request method IS POST, then it should reassign to form with post data being passed into it
        if form.is_valid():
            # print("The form is valid")
            # print(form.cleaned_data)
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # age = form.cleaned_data['age']
            # agent = form.cleaned_data['agent']
            # Lead.objects.create(
            #     first_name=first_name,
            #     last_name=last_name,
            #     age=age,
            #     agent=agent
            # )
            # print("Lead has been created")

            # As we have used LeadModelForm instead of LeadForm
            # we can avoid above commented boiler-plate code and
            # use just form.save() method
            form.save()
            return redirect("/leads")
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)
