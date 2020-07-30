from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
#from usuarios.models import Docente


@login_required
def home_d(request):
	current_user = request.user
	#instance = get_object_or_404(Docente, id_perfil_id = current_user.id)


	context = {

		"nom": current_user.first_name,
		"ape":current_user.last_name,
	}
	
	return render(request,"home_d.html",context)


@login_required
def logout_view(request):
    logout(request)
    return render(request,"main.html")
