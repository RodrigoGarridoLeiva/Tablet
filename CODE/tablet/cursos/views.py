from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def inicio_cursos(request):
	current_user = request.user
	#instance = get_object_or_404(Docente, id_perfil_id = current_user.id)


	context = {

		"nom": current_user.first_name,
		"ape":current_user.last_name,
	}
	
	return render(request,"inicio_cursos.html",context)
