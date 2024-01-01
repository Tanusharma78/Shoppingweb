from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import customerForm, ProductForm
from django.views.generic import UpdateView
from django.contrib import messages


def products(request):
    posts = Product.objects.all()
    posts = Product.objects.filter().order_by('-dateTime')
    return render(request, "products.html", {'posts':posts})

def products_comments(request, product_name):
    post = Product.objects.filter(product_name=product_name).first()
    comments = Comment.objects.filter(product=post)
    if request.method=="POST":
        user = request.user
        description = request.POST.get('description','')
        product_id =request.POST.get('product_id','')
        comment = Comment(user = user, description = description, product=post)
        comment.save()
    return render(request, "products_comments.html", {'post':post, 'comments':comments})

def Delete_product_Post(request, product_name):
    posts = Product.objects.get(product_name=product_name)
    if request.method == "POST":
        posts.delete()
        return redirect('/')
    return render(request, 'delete_product_post.html', {'posts':posts})

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(title__contains=searched)
        return render(request, "search.html", {'searched':searched, 'products':products})
    else:
        return render(request, "search.html", {})

@login_required(login_url = '/login')
def add_products(request):
    if request.method=="POST":
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            Product = form.save(commit=False)
            Product.author = request.user
            Product.save()
            obj = form.instance
            alert = True
            return render(request, "add_products.html",{'obj':obj, 'alert':alert})
    else:
        form=ProductForm()
    return render(request, "add_products.html", {'form':form})

class UpdatePostView(UpdateView):
    model = Product
    template_name = 'edit_product_post.html'
    fields = ['title', 'product_name', 'content', 'image']


def user_profile(request, myid):
    post = Product.objects.filter(id=myid)
    return render(request, "user_profile.html", {'post':post})

def Profile(request):
    return render(request, "profile.html")

def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method=="POST":
        form = customerForm(data=request.POST, files=request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            alert = True
            return render(request, "edit_profile.html", {'alert':alert})
    else:
        form=customerForm(instance=profile)
    return render(request, "edit_profile.html", {'form':form})


def signup(request):
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/signup')
        
        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, 'login.html')   
    return render(request, "signup.html")

def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
        return render(request, 'product.html')   
    return render(request, "login.html")

def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/login')