from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    return render(request, "front/home.html", {"year": datetime.date.today().year})
