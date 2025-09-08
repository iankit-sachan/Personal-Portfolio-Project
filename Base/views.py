from django.shortcuts import render
from django.http import HttpResponse #step 2

#Step 6 Create your views here.
def home(request): 
    return render(request, 'home.html')