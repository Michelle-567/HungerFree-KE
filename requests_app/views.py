

from django.shortcuts import render, redirect
from .forms import HelpRequestForm

def request_help_view(request):
    if request.method == "POST":
        form = HelpRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "requests_app/request_success.html")
    else:
        form = HelpRequestForm()
    return render(request, "requests_app/request_help.html", {"form": form})
