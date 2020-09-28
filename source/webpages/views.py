from django.shortcuts import render
from django.contrib.auth.decorators import login_required 

# Create your views here.


def home(request):
    return render(request, 'home.html')

@login_required
def tech(request):
    return render(request, 'tech.html')

def feedback(request):
    return render(request, 'feedback.html')
