import os
import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.conf import settings

# Defina o token de acesso (ou armazene-o de forma mais segura)
VALID_TOKEN = "Sua-Chave-Token-uuid-Aqui"

def consulta(request):
    # Obtenha os parametros 'token' e 'file' da URL
    token = request.GET.get('token')
    file_number = request.GET.get('file')

    # Verifique se o token e valido
    if token != VALID_TOKEN:
        return JsonResponse({'error': 'Invalid token'}, status=403)

    # Verifique se o parametro 'file' é fornecido e e um numero
    if not file_number or not file_number.isdigit():
        return HttpResponseBadRequest('Parametro "file" invalido ou ausente')

    # Construa o caminho do arquivo JSON
    #file_path = os.path.join(settings.BASE_DIR, 'json_files', f'file{file_number}.json')
    file_path = f'/opt/bee/beesoftDNS/tmp/{file_number}.json'

    # Verifique se o arquivo existe
    if not os.path.isfile(file_path):
        return JsonResponse({'error': 'File not found'}, status=404)

    # Carregue o conteudo do arquivo JSON e retorne como resposta
#    with open(file_path, 'r') as json_file:
#        data = json.load(json_file)
#    return JsonResponse(data)

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except:
        return JsonResponse({'Erro': 'Formato invalido do arquivo json...'}, status=500)

    if isinstance(data, list):
        return JsonResponse(data, safe=False)
    elif isinstance(data, dict):
        return JsonResponse(data, safe=True)
    else:
        return JsonResponse({'Erro': 'Formato invalido do arquivo json...'}, status=500)
