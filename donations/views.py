from django.shortcuts import render, redirect
from .models import Donation
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

def donate_view(request):
    return render(request, "donations/donate.html")

from django.shortcuts import render, redirect
from .forms import DonationForm

def donate_form_view(request):
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DonationForm()
    return render(request, "donations/donate_form.html", {"form": form})



@login_required
def make_donation(request):
    if request.method == "POST":
        donation_type = request.POST.get("donation_type")
        description = request.POST.get("description")
        amount = request.POST.get("amount") if donation_type == "money" else None
        
        Donation.objects.create(
            donor=request.user,
            donation_type=donation_type,
            description=description,
            amount=amount
        )
        return redirect("donation_list")
    
    return render(request, "donations/make_donation.html")

@login_required
def donation_list(request):
    donations = Donation.objects.all().order_by("-created_at")
    return render(request, "donations/donation_list.html", {"donations": donations})
