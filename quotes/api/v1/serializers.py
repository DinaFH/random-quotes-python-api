
from rest_framework import serializers
from quotes.models import Quote



class QuoteSerializer(serializers.ModelSerializer):
    # inner class called meta to describe data of the model
    class Meta:
        model = Quote
        fields = '__all__'
        depth = 1