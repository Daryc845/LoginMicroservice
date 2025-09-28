from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Users

# Permitir POST sin CSRF (solo para pruebas)
@csrf_exempt
def CreateUser(request):
    if request.method == "POST":
        data = json.loads(request.body)
        userid = data.get("userid")
        password = data.get("password")
        
        if not userid or not password:
            return JsonResponse({"userCreated": False, "message": "Falta el userid o la contraseña"})
        
        # Verificar si ya existe
        if Users.objects.filter(userid=userid).exists():
            return JsonResponse({"userCreated": False, "message": "El usuario ya existe"})
        
        # Crear usuario
        Users.objects.create(userid=userid, password=password)
        return JsonResponse({"userCreated": True})
    
    return JsonResponse({"userCreated": False, "message": "Método invalido"})


@csrf_exempt
def AuthUser(request):
    if request.method == "POST":
        data = json.loads(request.body)
        userid = data.get("userid")
        password = data.get("password")
        
        # Verificar usuario
        user = Users.objects.filter(userid=userid, password=password).first()
        if user:
            return JsonResponse({"userCreated": True})
        else:
            return JsonResponse({"userCreated": False})
    
    return JsonResponse({"userCreated": False, "message": "Invalid method"})
