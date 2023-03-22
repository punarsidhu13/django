from django.shortcuts import render, redirect
from .form import AmazonForm, CreateNewUserForm
from .models import Amazon
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate



#Create your views here.

def home_page(request):
    return render(request,'home.html',{})

def create_inventory(request):
    form = AmazonForm()
    if request.method == "POST":
        form = AmazonForm(request.POST)
        form.save()
    return render(request, 'inventory.html', {'form':form})


def list_inventory(request):
    list = Amazon.objects.all()                                                  
    return render(request, 'list.html', {'lists':list})

def add_to_cart(request, **kwargs):
    if pk:= kwargs.get('pk'):
        product = Amazon.objects.get(pk = pk)
        cart = request.session.get('cart',[])
        item = {'name_of_product':product.name, 'Price':product.price, 'ID':product.pk}
        cart.append(item)
        request.session['cart'] = cart
        name = request.session['cart']
    return render(request,'cart.html', {'names':name})
    
def remove_from_cart(request, **kwargs):
    
    if pk := kwargs.get('pk'):
        product = Amazon.objects.get(pk = pk)
        for i in request.session['cart']:
            if i['ID'] == product.pk:
                # import pdb;pdb.set_trace()
                request.session['cart'].remove(i)
                name = request.session['cart']
    return render(request, 'cart.html', {'names':name})



def create_new_user(request):
    # import pdb;pdb.set_trace()
    form = CreateNewUserForm()
    if request.method == 'POST':
        form = CreateNewUserForm(request.POST)
        # print(request.user)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email')
        user = User.objects.create_user(username, password=password, email=email)
        user.save()
        return redirect('home')
    return render(request,'register.html', {'form':form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        print('======================>')
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    return redirect("home")

def cart_details(request):
    name = request.session['cart']
    return render(request,'cart.html',{'names':name})