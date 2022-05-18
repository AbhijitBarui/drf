import json
# from django.http import JsonResponse,HttpResponse
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request,*args,**kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.data)
        data=serializer.data
        return Response(data)
    else:
        return Response(request.data)