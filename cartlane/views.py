from django.shortcuts import render, redirect
from jewellery.forms import ProductForm, DiamondForm
from jewellery.models import Category, Sub_Category, Product, UserCreateForm, Diamond
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.core.paginator import Paginator, EmptyPage
from jewellery.filters import DiamondFilter
# from jewellery.forms import DiamondFilterForm

# Create your views here.

def Master(request):
    category = Category.objects.all()
    
    context = {
        'category': category
    }
    
    return render(request, 'master.html',context)


def Index(request):
    category = Category.objects.all()
    
    favourite = Product.objects.all().filter(favourite=True)[0:6]

    categoryID = request.GET.get('category')
    
    diamond = Diamond.objects.all().order_by('-id')[:6]

    if categoryID:
        product = Product.objects.filter(sub_category= categoryID).order_by('-id')
    else:
        product = Product.objects.all().order_by('-id')

    context = {
        'category': category,
        'product': product,
        'favourite': favourite,
        'diamond': diamond,
    }

    return render(request, 'index.html', context)



def category(request, id):
    category1 = Category.objects.get(id= id)
    
    category = Category.objects.all()
    
    category_product = Product.objects.filter(category= category1)
    
    sub_Category = Sub_Category.objects.filter(category=category1)
    
    subcategoryID = request.GET.get('subcategory')
    
    if subcategoryID:
        category_product = Product.objects.filter(sub_category= subcategoryID).order_by('-id')
    else:
        category_product = Product.objects.filter(category= category1)
    
    
    context = {
        'category1': category1,
        'category': category,
        'product1': category_product,
        'sub_Category': sub_Category,
    }
    
    return render(request, 'product/product.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.isvalid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],

            )
            login(request, new_user)
            return redirect('index') 
    else:
        form = UserCreateForm()

    context = {
        'form':form
    }        
    return render(request, 'registration/signup.html', context)  


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')

        else: 
            messages.info(request,'Passward Not Matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'registration/register.html') 


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Creditonsl')
            return redirect('login')
    else:
        return render(request, 'registration/login.html') 

def logout(request):
    auth.logout(request)
    return redirect('/')




# AddtoCart

@login_required(login_url="/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')




def product_details(request, id):
    category = Category.objects.all()

    product = Product.objects.filter(id= id).first()
    
    random_object = Product.objects.order_by('?')[:6]

    context = {
        'category': category,
        'product': product,
        'random_object': random_object,
    }
    return render(request,'product/product_details.html', context)



# Inventory

def inventory_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('inventory')
        else:
            messages.info(request,'Invalid Creditonsl')
            return redirect('inventory_login')
        
    return render(request, 'registration/inventory_login.html') 



@login_required(login_url="/inventory_login")
def inventory(request):
    category = Category.objects.all()
    
    categoryID = request.GET.get('category')
    
    diamond = Diamond.objects.all().order_by('-id')
    
    p = Paginator(diamond, 2)
    
    page_number = request.GET.get('page', 1)
    
    diamond_all = p.page(page_number)

    product = Product.objects.all().order_by('-id')
    pagi = Paginator(product, 5)
    page_no = request.GET.get('productpage', 1)
    product_all = pagi.page(page_no)
    
    
    context = {
        'category': category,
        'product': product_all,
        'diamond': diamond_all,
    }
    
    return render(request,'product/inventory.html', context)

def inventory_add(request):  
    form = ProductForm()
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("SUccesfull")
            return redirect('inventory')
        
    else:
        form = ProductForm()
        print("Error")
        
    context = {
        'form' : form
    }
    
    return render(request,'inventory/inventory_add.html', context)  
 

def inventory_update(request, id):  
    product = Product.objects.get(id=id)  
    
    form = ProductForm(instance=product)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            print("Succesfull Inserted")
            return redirect('inventory')
    
    context = {
        'form': form
    }

    return render(request, 'inventory/inventory_edit.html', context)  

def inventory_delete(request, id):  
    product = Product.objects.get(id=id)
    product.delete()  
    return redirect('inventory')


# Diamond

def diamond(request):
    
    category = Category.objects.all()
    
    diamond_filter = DiamondFilter(request.GET, queryset= Diamond.objects.all())
    
    diamond = diamond_filter.qs
        
    paginator = Paginator(diamond, 5)
    
    page_num = request.GET.get('page', 1)
    
    try:
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(1)
        
    context = {
        'form': diamond_filter.form,
        'category': category,
        'page_num': page_num,
        'all_page': paginator.num_pages,
        'items': page,
        'diamond': diamond_filter.qs
    }
    return render(request, 'diamond/diamond.html',context)



def diamond_add(request):  
    form = DiamondForm()
    
    if request.method == 'POST':
        form = DiamondForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("SUccesfull")
            return redirect('inventory')
        
    else:
        form = DiamondForm()
        print("Error")
        
    context = {
        'form' : form
    }
    
    return render(request,'diamond/diamond_add.html', context)      

def diamond_details(request, id):
    category = Category.objects.all()

    diamond = Diamond.objects.filter(id= id).first()
    
    random_object = Diamond.objects.order_by('?')[:6]
    
    context = {
        'category': category,
        'diamond': diamond,
        'random_object': random_object,
    }
    return render(request,'diamond/diamond_details.html', context)


def diamond_update(request, id):  
    diamond = Diamond.objects.get(id=id)  
    
    form = DiamondForm(instance=diamond)
    
    if request.method == 'POST':
        form = DiamondForm(request.POST, request.FILES, instance=diamond)
        if form.is_valid():
            form.save()
            print("Succesfull Inserted")
            return redirect('inventory')
    
    context = {
        'form': form
    }

    return render(request, 'diamond/diamond_edit.html', context)  

def diamond_delete(request, id):  
    diamond = Diamond.objects.get(id=id)
    diamond.delete()  
    return redirect('inventory')


def search(request):
    query = request.GET['query']
    product = Product.objects.filter(name__icontains = query)
    context = {
        'product': product,
    }
    return render(request,'search.html', context)