from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.decorators import api_view

@api_view(['POST'])
def signup(request):
    response={'data':None,'status':status.HTTP_400_BAD_REQUEST}
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response['data']=serializer.data
        response['status']=status.HTTP_201_CREATED
    else:
        response['data']=serializer.errors
    return Response(**response)