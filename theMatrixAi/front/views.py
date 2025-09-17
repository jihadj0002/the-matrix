from django.shortcuts import render
import datetime
from django.http import HttpResponse
from .models import Contact
from django.core.mail import send_mail  # optional if you want email

# Create your views here.
def home(request):
    return render(request, "front/home.html", {"year": datetime.date.today().year})

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