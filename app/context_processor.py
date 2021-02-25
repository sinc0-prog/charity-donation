from .models import *
from django.contrib.auth import *

def all_donation(request):
    donation = 0
    try:
        donation = Donation.objects.all().count()
    except Exception: pass
    return {"donation_quantity": donation }

def all_institution(request):
    quantity_institution = 0
    try:
        institution = Institution.objects.all().count()
    except Exception: pass
    return {'quantity_institution': quantity_institution}