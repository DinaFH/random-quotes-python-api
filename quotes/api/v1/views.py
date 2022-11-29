from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.http import JsonResponse
from quotes.models import Quote
from .serializers import QuoteSerializer
import random

#functiona_based views:
@api_view(['GET'])
def hello_drf(request):
    return Response(data={"message":"hello world"},status=status.HTTP_200_OK)

@api_view(['GET'])
def generate_all(request, format=None):
    random_quotes = Quote.objects.all()
    serializer = QuoteSerializer(random_quotes, many=True)
    return JsonResponse({"random quotes": serializer.data}, safe=False,status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def generate_random(request):
    random_id=random.randint(1,10)
    quote_object=Quote.objects.get(pk=random_id)
    serializer = QuoteSerializer(quote_object)
    return JsonResponse({"random quotes": serializer.data}, safe=False,status=status.HTTP_200_OK)
