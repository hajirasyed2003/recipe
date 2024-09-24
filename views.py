from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib import messages #type: ignore
from django.contrib.auth import authenticate, login, logout #type: ignore 
from django.contrib.auth.decorators import login_required #type: ignore 
from .models import *

# Create your views here.

@login_required(login_url="/login/")
def recipes(request):
    if request.method == "POST":
        data=request.POST
        recipe_image=request.FILES.get('recipe_image')
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')

        
        Recipe.objects.create(
            recipe_image=recipe_image,
            recipe_name=recipe_name,
            recipe_description=recipe_description,
        )

        return redirect('/recipes/')
    queryset=Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains=request.GET.get('search'))

    context = {'recipes': queryset}
    return render(request,'recipes.html',context)

@login_required(login_url="/login/")
def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        recipe_image=request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description= data.get('recipe_description')

        if recipe_image:
            queryset.recipe_image= recipe_image
        
        queryset.recipe_name=recipe_name
        queryset.recipe_description=recipe_description

        queryset.save()
        return redirect('/recipes/')

    context = {'recipe': queryset}
    return render(request, 'update_recipes.html', context)

@login_required(login_url="/login/")
def delete_recipe(request, id):
    queryset=Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')

def login_page(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request,"Invalid Username")
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/recipes/')
        
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        username= request.POST.get('username')
        password= request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already exists!")
            return redirect('/register/')

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )

        user.set_password(password)
        user.save()
        messages.info(request, "Account created Successfully!")
        return redirect('/register/')

    return render(request, 'register.html')
