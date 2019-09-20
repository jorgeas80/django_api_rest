from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Category


def category_list(request):
    # We may need a filter...
    #data = serialize('json', Category.objects.all())
    data = serialize('json', Category.objects.all(), fields=('name', 'description'))

    return HttpResponse(data, content_type='application/json')


def category_list_2(request):
    # We may need a filter...
    data = list(Category.objects.values('active', 'name', 'description'))
    return JsonResponse(data, safe=False)


def category_detail(request, pk):
    data = serialize('json', Category.objects.filter(pk=pk))
    return HttpResponse(data, content_type='application/json')

def category_detail_2(request, pk):
    data = list(Category.objects.filter(pk=pk).values('active', 'name', 'description'))
    return JsonResponse(data[0], safe=False)

def category_detail_3(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    data = {
        'active': cat.active,
        'name': cat.name,
        'description': cat.description
    }
    print(data)
    return JsonResponse(data)
