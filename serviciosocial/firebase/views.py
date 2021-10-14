from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from api.serializers import CategorySerializer, ProductSerializer, QuerySerializer
from api.models import Category, Product, Query
from firebase.settings import init_firebase
from firebase_admin import db
import json


@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        return JsonResponse({'test': 'test'}, safe=False)

    elif request.method == 'POST':
        return JsonResponse({'error': "Error"}, status=400)


@csrf_exempt
def snippet_detail(request, model):
    path = "Servicio/"+model
    if not path_exists(path):
        return HttpResponse({'error': 'path not exist'}, status=404)

    elif request.method == 'POST':
        body = json.loads(request.body)
        data = get_required_data(model)
        return process_query(data, body, path)


@csrf_exempt
def query_loader(request, id):
    if request.method == 'GET':
        object = Query.objects.get(pk=id)
        query = QuerySerializer(object).data
        init_firebase(query["url"])
        path = "Servicio/"+query["table"]
        if not path_exists(path):
            return HttpResponse({'error': 'path not exist'}, status=404)
        data = get_required_data(query["table"])
        return process_query(data, query, path)
    return JsonResponse({'msg': 'Method not allowed'}, status=400)


@csrf_exempt
def table_loader(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        init_firebase()
        data = db.reference("Servicio/"+body["node"].capitalize()).get()
        for object in data.items():
            object[1][body["key"]] = object[0]
            load_data_to(object[1], body["node"].capitalize())
        return JsonResponse({'msg': 'Method Allowed'}, status=200)
    return JsonResponse({'msg': 'Method not allowed'}, status=400)


def insert_data_to(value, path="Servicio/", key="test"):
    return db.reference(path).child(key).set(value)


def path_exists(path="Servicio/"):
    return db.reference(path).get()


def get_required_data(model):
    if model == 'Products':
        products = Product.objects.values()
        return ProductSerializer(products, many=True).data
    elif model == 'Categories':
        categories = Category.objects.all()
        return CategorySerializer(categories, many=True).data
    else:
        return []


def process_data(data, path, node, fields=None):
    for object in data:
        key = str(object.get(node))
        del object[node]
        if fields:
            object = {key: object[key] for key in object.keys() & fields}
            insert_data_to(object, path, key)
        else:
            insert_data_to(object, path, key)


def process_query(data, query, path):
    if len(data) > 0:
        if(query['truncate']):
            db.reference(path).delete()
        try:
            process_data(data, path, query['node'], query['fields'])
        except:
            process_data(data, path, query['node'])
        return JsonResponse({'message': 'info uploaded succesfully'}, status=200)
    return JsonResponse({'error': 'no data to process'}, status=404)


def load_data_to(object, model):
    del object["id"]
    if model == 'Products':
        p = Product()
        for key, value in object.items():
            setattr(p, key, value)
        p.save()
    elif model == 'Categories':
        if object["products"] is not None:
            del object["products"]
        cat = Category()
        for key, value in object.items():
            setattr(cat, key, value)
        cat.save()
    else:
        return []
