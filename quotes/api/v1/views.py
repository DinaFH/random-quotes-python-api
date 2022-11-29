from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


#functiona_based views:
@api_view(['GET'])
def hello_drf(request):
    return Response(data={"message":"hello world"},status=status.HTTP_200_OK)