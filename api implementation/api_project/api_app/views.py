from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import ItemSerializer
from rest_framework import serializers
from rest_framework import status
from . models import Student


@api_view(['GET'])
def ApiOverview(request):
          api_urls = {
                    'all_items': 'all',
                    'Search by Category': '/?category=category_name',
                    'Search by Subcategory': '/?subcategory=category_name',
                    'Add': '/create',
                    'Update': '/update/pk',
                    'Delete': '/item/pk/delete'
          }
          return Response(api_urls)


@api_view(['POST'])
def add_items(request):
    Items = ItemSerializer(data=request.data)
 
    # validating for already existing data
    if Student.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if Items.is_valid():
        Items.save()
        return Response(Items.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def view_items(request):
     
     
    # checking for the parameters from the URL
    if request.query_params:
        items = Student.objects.filter(**request.query_params.dict())
    else:
        items = Student.objects.all()
 
    # if there is something in items else raise error
    if items:
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['POST'])
def update_items(request, pk):
    item = Student.objects.get(pk=pk)
    data = ItemSerializer(instance=item, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)    

@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(Student, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)