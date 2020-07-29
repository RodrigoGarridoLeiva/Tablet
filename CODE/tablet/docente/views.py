from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def home_d(request):
	
	return render(request,"home_d.html")


@login_required
def logout_view(request):
    logout(request)
    return render(request,"main.html")
