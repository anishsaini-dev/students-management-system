from django.shortcuts import render
from .models import Profile
def bade(request):
    return render(request, 'myapp/bade.html')
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'myapp/profile_list.html', {'profiles': profiles})