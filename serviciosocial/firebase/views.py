from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from api.serializers import CategorySerializer, ProductSerializer
from api.models import Category, Product
from firebase_admin import db
import json


@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        return JsonResponse({'test': 'test'}, safe=False)

    elif request.method == 'POST':
        return JsonResponse({'error': "Erro"}, status=400)


@csrf_exempt
def snippet_detail(request, model):
    path = "Servicio/"+model
    if not path_exists(path):
        return HttpResponse({'error': 'path not exist'}, status=404)

    elif request.method == 'POST':
        body = json.loads(request.body)
        data = get_required_data(model)
        if len(data) > 0:
            process_data(data, path, body['node'])
            return JsonResponse({'message': 'info uploaded succesfully'}, status=200)
        return JsonResponse({'error': 'no data to process'}, status=404)


def insert_data_to(value, path="Servicio/", key="test"):
    return db.reference(path).child(key).set(value)


def path_exists(path="Servicio/"):
    return db.reference(path).get()


def get_required_data(model):
    if model == 'Products':
        return Product.objects.values()
    elif model == 'Categories':
        return Category.objects.values()
    else:
        return []


def process_data(data, path, node):
    for object in data:
        key = str(object.get(node))
        del object[node]
        insert_data_to(object, path, key)