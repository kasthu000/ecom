from django.shortcuts import render, redirect, get_object_or_404

# Create views 
from  . models import Product
from . forms import ProductForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

# Create your views here.

from django.contrib.auth import authenticate, login , logout

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired home page URL
        else:
            error_message = 'Invalid username or password.'
    else:
        error_message = None

    return render(request, 'accounts/login.html', {'error_message': error_message})




def home(request):
    return render(request,'accounts/home.html', {'userName' : request.user.username})




def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Replace 'login' with the name of your login URL pattern
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})

def logout_user(request):
    logout(request)
    #return redirect('login')
    return redirect('home')


@login_required
def product_list(request): # landing page
    products = Product.objects.all()
    return render(request,'product_list.html',{'products': products})
@login_required
def product_detail(request, id): #detailed view
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})
@login_required
def product_create(request):  #Create the product
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})
@login_required
def product_update(request, id):  #Update the product
    products = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=products)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=products)
    return render(request, 'product_form.html', {'form': form})
@login_required
def product_delete(request, id):  # Delete the product
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        
        return redirect('product_list')
    return render(request, 'product_delete.html', {'product': product})


