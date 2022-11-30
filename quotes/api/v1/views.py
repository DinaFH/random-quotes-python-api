from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.http import JsonResponse
from quotes.models import Quote
from .serializers import QuoteSerializer
import random
import xlsxwriter
import datetime

my_dictionary={}
#functiona_based views:

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def generate_all(request, format=None):
    random_quotes = Quote.objects.all()
    serializer = QuoteSerializer(random_quotes, many=True)
    return JsonResponse({"random quotes": serializer.data}, safe=False,status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def generate_random(request):
    random_id = random.randint(1, 10)
    quote_object=Quote.objects.get(pk=random_id)
    serializer = QuoteSerializer(quote_object)
    
    #saving the number of times each quote was picked in a dictionary
    if random_id in my_dictionary:
        my_dictionary[random_id] = my_dictionary[random_id] + 1
    else:
        my_dictionary[random_id] = 1
    print(my_dictionary)

    #calculating total number of calls
    total_calls = 0
    for x in my_dictionary:
     total_calls = total_calls + my_dictionary[x]
    print(total_calls)

  #if total number of calls become 10 create excel file
    if(total_calls==10):
      now = datetime.datetime.now()
      current_date=str(now.year)+'_'+str(now.month)+'_'+str(now.day)+'_'+str(now.hour)+'_'+str(now.second)
      file_name='quotes_api_report'+current_date
      with xlsxwriter.Workbook(f'{file_name}.xlsx') as workbook:
        worksheet = workbook.add_worksheet('Quote Report')
        worksheet.write(0, 0, 'QuoteID')
        worksheet.write(0, 1, 'Count')
        for i, (k, v) in enumerate(my_dictionary.items(), start=1):
            worksheet.write(i, 0, k)
            worksheet.write(i, 1, v)


    return JsonResponse({"random quotes": serializer.data}, safe=False,status=status.HTTP_200_OK)




