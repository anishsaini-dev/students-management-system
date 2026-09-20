from django.shortcuts import render 

def router(request):
    return render(request , 'computer/router.html')