from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import PostCreateSerializer

@api_view(['POST'])
def create_post(request):
    serializer = PostCreateSerializer(data=request.data)
    
    # is_valid : serializer에서 필요로하는 field값이 잘 들어왔는지...
    if serializer.is_valid():
        # db에 저장(python 객체를)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)