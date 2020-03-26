from rest_framework import serializers
from .models import Stock


class StockSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stock
        # for specific fields
        # fields = ('ticker', 'volume')
        # for all fields
        fields = '__all__'
