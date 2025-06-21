from django.shortcuts import render
from .models import Sponsor

def sponsors_list(request):
    sponsors = Sponsor.objects.all()
    return render(request, 'sponsors/sponsors.html', {'sponsors': sponsors})
