from itertools import product
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework. response import Response
from rest_framework import status
from .serializers import SuperSerializer

from .models import Super

@api_view(['GET'])
def supers_list(request):

    if request.method == 'GET':
        supers = Super.objects.all()
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)