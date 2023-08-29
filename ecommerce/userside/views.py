from django.shortcuts import render
from .models import Mobile 

def homepage(request):
    mobiles = Mobile.objects.all()  # Fetch all mobile objects from the database

    context = {'mobiles': mobiles}
    return render(request, 'home.html', context)
# showing product detailes 
def product_detail(request, mobile_id):
    mobile = Mobile.objects.get(pk=mobile_id)
    context = {'mobile': mobile}
    return render(request, 'products_detail.html', context)