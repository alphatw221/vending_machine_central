from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import *
from .serializers import *

#----------------------------------------------寫法一-------------------------------------
# from dajango.shortcuts import JsonResponse
# from rest_framework.parser import JSONParser

# @csrf_exempt
# def product_list(request):

#     if request.method == 'GET':
#         products=Product.objects.all()
#         serializer=ProductSerializer(products,many=True)
#         return JsonResponse(serializer.data,safe=False)

#     elif request.method == 'POST':
#         data=JSONParser().parse(request)
#         serializer=ProductSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201)
#         return JsonResponse(serializer.errors,status=400)

# @csrf_exempt
# def product_detail(request,pk):
#     try:
#         product=Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         return HttpTesponse(status=404)

#     if request.method=='GET':
#         serializer=ProductSerializer(product)
#         return JsonResponse(serializer.data)

#     elif request.method=='PUT':
#         data=JSONParser().parse(request)
#         serializer=ProductSerializer(product,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors,status=400)

#     elif request.method=='DELETE':
#         product.delete()
#         return HttpTesponse(status=204)


#-----------------------------------------------------寫法二-----------------------------------------
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# @api_view(['GET','POST'])
# def product_list(request):

#     if request.method == 'GET':
#         products=Product.objects.all()
#         serializer=ProductSerializer(products,many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer=ProductSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT''DELETE'])
# def product_detail(request,pk):
#     try:
#         product=Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         return HttpTesponse(status=HTTP_404_NOT_FOUND)

#     if request.method=='GET':
#         serializer=ProductSerializer(product)
#         return Response(serializer.data)

#     elif request.method=='PUT':
#         serializer=ProductSerializer(product,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     elif request.method=='DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#------------------------------------------------------寫法三-----------------------------------
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


def login_page(request):
    
    context={}
    return render(request,'login_page.html',context)

def control_panel(request):
    key=request.COOKIES.get('token')
    try:
        token=Token.objects.get(key=key)
    except Token.DoesNotExist:
        return render(request,'login_page.html')

    context={'products':Product.objects.all(),'machines':Machine.objects.all(),'transactions':Transaction.objects.all(),'restocks':Restock.objects.all()}
    return render(request,'control_panel.html',context)

#--------------------------------------api----------------------------------------------------

class Login(APIView):
    def post(self,request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            try:
                token=Token.objects.get(user=user)
                token.delete()
            except Token.DoesNotExist:
                pass
            
            token=Token.objects.create(user=user)

            content={'token':token.key}
            return Response(content)
        return Response('登入失敗')
        

class Logout(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def post(self,request):
        key=request.headers['Authorization'][6:]
        token=Token.objects.get(key=key)
        token.delete()
        content={'message':'登出成功'}
        return Response(content)
        

class ProductList(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request):
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            content={'message':'新增成功','data':serializer.data}
            # return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductDetails(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get_object(self,id):
        try:
            product=Product.objects.get(id=id)
            return product
        except Product.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self,request,id):
        product=self.get_object(id)
        serializer=ProductSerializer(product)
        return Response(serializer.data)

    def put(self,request,id):
        product=self.get_object(id)
        serializer=ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={'message':'更新成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        product=self.get_object(id)
        product.delete()
        content={'message':'刪除成功'}
        return Response(content)
        # return Response(content,status=status.HTTP_204_NO_CONTENT)
        

class MachineList(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request):
        machines=Machine.objects.all()
        serializer=MachineSerializer(machine,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=MachineSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            content={'message':'新增成功','data':serializer.data}
            # return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class MachineDetails(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get_object(self,id):
        try:
            machine=Machine.objects.get(id=id)
            return machine
        except Machine.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self,request,id):
        machine=self.get_object(id)
        serializer=MachineSerializer(machine)
        return Response(serializer.data)

    def put(self,request,id):
        machine=self.get_object(id)
        serializer=MachineSerializer(machine,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={'message':'更新成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        machine=self.get_object(id)
        machine.delete()
        content={'message':'刪除成功'}
        return Response(content)
        # return Response(content,status=status.HTTP_204_NO_CONTENT)

class MachineAddProduct(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get_machine(self,id):
        try:
            machine=Machine.objects.get(id=id)
            return machine
        except Machine.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get_product(self,id):
        try:
            product=Product.objects.get(id=id)
            return product
        except Product.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def post(self,request,id):
        machine=self.get_machine(id)
        product=self.get_product(request.data['product_id'])
        
        machine.products.add(product)
        content={'message':'增加商品成功'}
        return Response(content)

class TransactionList(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request):
        transaction=Transaction.objects.all()
        serializer=TransactionSerializer(transaction,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=TransactionSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            content={'message':'新增成功','data':serializer.data}
            # return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TransactionDetails(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get_object(self,id):
        try:
            transaction=Transaction.objects.get(id=id)
            return transaction
        except Transaction.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self,request,id):
        transaction=self.get_object(id)
        serializer=TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self,request,id):
        transaction=self.get_object(id)
        serializer=TransactionSerializer(transaction,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={'message':'更新成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        transaction=self.get_object(id)
        transaction.delete()
        content={'message':'刪除成功'}
        return Response(content)
        # return Response(content,status=status.HTTP_204_NO_CONTENT)

class RestockList(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request):
        restock=Restock.objects.all()
        serializer=RestockSerializer(machine,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=RestockSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            content={'message':'新增成功','data':serializer.data}
            # return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class RestockDetails(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get_object(self,id):
        try:
            restock=Restock.objects.get(id=id)
            return restock
        except Restock.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self,request,id):
        restock=self.get_object(id)
        serializer=RestockSerializer(machine)
        return Response(serializer.data)

    def put(self,request,id):
        restock=self.get_object(id)
        serializer=RestockSerializer(restock,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={'message':'更新成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        restock=self.get_object(id)
        restock.delete()
        content={'message':'刪除成功'}
        return Response(content)
        # return Response(content,status=status.HTTP_204_NO_CONTENT)