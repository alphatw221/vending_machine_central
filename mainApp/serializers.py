from rest_framework import serializers
from .models import *

# class  ProductSerializer(serializers.Serializer):

#     name=serializers.CharField(max_length=30)
#     sale_price=serializers.IntegerField()
#     purchase_price=serializers.IntegerField()
#     stock=serializers.IntegerField()
#     description=serializers.TextField()
    
#     machines=serializers.ManyToManyField('Machine',blank=True, null=True)
    
#     def create(self,validated_data):
#         return Product.objects.create(validated_data)

#     def update(self,instance,validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.sale_price=validated_data.get('sale_price',instance.sale_price)
#         instance.purchase_price=validated_data.get('purchase_price',instance.purchase_price)
#         instance.stock=validated_data.get('stock',instance.stock)
#         instance.description=validated_data.get('description',instance.description)
#         instance.save()
#         return instance




class  ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class  MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Machine
        fields='__all__'

class  TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields='__all__'

class  RestockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Restock
        fields='__all__'
