from django.shortcuts import render

def partners_view(request):
    return render(request, 'partners/partners.html')
