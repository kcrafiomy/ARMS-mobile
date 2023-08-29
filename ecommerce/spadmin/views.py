from django.shortcuts import render, redirect
from .forms import MobileForm
from userside.models import Mobile,Category  # Import the Mobile model

def adminhome(request):
    
    return render(request, 'adminhome.html')

def dataAdd(request):  # Corrected the parameter name to 'request'
    if request.method == 'POST':
        form = MobileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('spadmin')
    else:
        form = MobileForm()

    mobiles = Mobile.objects.all()  # Moved outside of the 'else' block

    context = {'form': form, 'mobiles': mobiles}
    return render(request, 'addproducts.html', context)
def edit_data(request, mobile_id):
    mobile = Mobile.objects.get(pk=mobile_id)

    if request.method == 'POST':
        form = MobileForm(request.POST, request.FILES, instance=mobile)
        if form.is_valid():
            form.save()
            return redirect('spadmin')
    else:
        form = MobileForm(instance=mobile)

    context = {'form': form}
    return render(request, 'edit_data.html', context)

def allproducts(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'allproducts.html', context)

def delete_product(request, mobile_id):
    mobile = Mobile.objects.get(pk=mobile_id)
    
    if request.method == 'POST':
        mobile.delete()
        return redirect('spadmin')  # Redirect to admin page after deletion
    
    context = {'mobile': mobile}
    return render(request, 'delete_product.html', context)


