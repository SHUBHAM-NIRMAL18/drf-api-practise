from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BookModel
from rest_framework import serializers


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'
    
    def validate(self, data):
        price = data['price']
        if price < 0:
            raise serializers.ValidationError("Price must be a positive number")
        return data

@api_view(['GET'])
def BookListApi(request):
    books = BookModel.objects.all()
    serializer = BookModelSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def BookCreateApi(request):
    data = request.data
    
    serializer = BookModelSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Book created successfully'})
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def BookUpdateApi(request, id):
    data = request.data

    book = BookModel.objects.get(id=id)
    
    serializer = BookModelSerializer(instance=book, data=data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Book updated successfully'})
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def BookDeleteApi(request, id):
    book = BookModel.objects.get(id=id)
    book.delete()
    return Response({'message': 'Book deleted successfully'})