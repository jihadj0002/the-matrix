from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
import datetime
from django.http import HttpResponse
from .models import Contact
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail  # optional if you want email

# Create your views here.
def home(request):
    context = {
        "year": datetime.date.today().year,
        "matrixai_logo_url": f"{settings.MEDIA_URL}images/matrixai.png"
    }
    


    return render(request, "front/home01.html", context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        business = request.POST.get("business")

        # 🔹 Option 1: Just print (debugging)
        #print(f"New Contact → {name}, {email}, {business}")

        # 🔹 Option 2: Save into DB (make a model)
        Contact.objects.create(name=name, email=email, business=business)

        # 🔹 Option 3: Send email notification
        # send_mail(
        #     f"AI Agent Demo Request from {name}",
        #     f"Business: {business}\nEmail: {email}",
        #     "your@email.com",
        #     ["yourother@email.com"],
        # )

        return HttpResponse("✅ Thank you! We’ll contact you soon.")
    
    return HttpResponse("❌ Invalid request.")

def dashboard(request):
    return render(request, "front/dashboard.html", {"user": request.user})


def c_dashboard(request):
    return render(request, "front/c_dashboard.html", {"user": request.user})



def login_view(request):
    print("Login open")
    if request.user.is_authenticated:
        return redirect('home')  # Redirect if already logged in
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print("Login successful")
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                
               
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
                print("Login successful")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
        # Store next URL from GET parameter
        next_url = request.GET.get('next', '')
    
    return render(request, 'front/login.html', {
        'form': form,
        'next': next_url
    })

def logout_view(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('home')