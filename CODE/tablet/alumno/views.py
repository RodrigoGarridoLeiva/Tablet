from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def home_l(request):
	
	return render(request,"home_l.html")

	
@login_required
def logout_view(request):
    logout(request)
    return render(request,"main.html")