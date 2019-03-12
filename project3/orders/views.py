from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Category, Regular_pizza, Sicilian_pizza, Salad, Pasta, Dinner_platter, Topping, Sub, User_order, Order2, Order_counter
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import login,logout, authenticate

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, "pizza/login_view.html", { "message": None})
    
    context = {
            "user" : request.user,
            "category" : Category.objects.all()
    }
    return render(request, "pizza/user.html", context)

def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index")) 
    else:
        return render(request, "pizza/login_view.html", {"message": "Inavalid credentials"})

def logout_view(request):
    logout(request)
    return render(request, "pizza/login_view.html", {"message": "loggedout"})

def signup_view(request):
        if request.method == "POST":
                first_name = request.POST.get("firstname")
                last_name = request.POST.get("lastname")
                user_name = request.POST.get("username")
                email_address = request.POST.get("emailaddress")
                pass_word1 = request.POST.get("password1")
                password2 = request.POST.get("password2")
                if pass_word1 != password2:
                        return render(request, "pizza/signup_view.html", {"message" :"passwords doesn't match"})
                user = User.objects.create_user(user_name,email_address, pass_word1)
                user.first_name = first_name
                user.last_name = last_name
                user.save() 
                return render (request, "pizza/login_view.html", {"message": "you're registered now please login"})
        return render(request, "pizza/signup_view.html",{"message": "please register"})


def menu_view(request, category_id ):
        context = {
                "user": request.user, 
                "message": None,
                "category": Category.objects.all(),
                "regular_pizza": Regular_pizza.objects.all(),
                "sicilian_pizza": Sicilian_pizza.objects.all(),
                "topping": Topping.objects.all(),
                "sub": Sub.objects.all(),
                "pasta": Pasta.objects.all(),
                "salad": Salad.objects.all(),
                "dinner_platter": Dinner_platter.objects.all()
        }
        return render(request, "pizza/menu.html", context)


        

