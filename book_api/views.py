from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def book_list(request):
    
    books = Book.objects.all() #complex data
    
    serializer = BookSerializer(books,many=True)
    return Response(serializer.data) 

@api_view(['POST'])  
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer)
    
@api_view(['GET', 'PUT', 'DELETE'])
def book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        book.delete()
        return JsonResponse({'message': 'Book deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
from rest_framework.views import APIView
from book_api.models import Book
from book_api.serializer import BookSerializer 
from rest_framework.response import Response 

class BookList(APIView):
    
    def get(self,request):
        books = Book.objects.all() #complex data
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data) 
    
class BookCreate(APIView):
        def post(self,request):
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
            else:
                return Response(serializer)
    
class BookDetail(APIView):
    
    def get_book_by_pk(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)

        
    def get(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
        
    def put(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete (self, request, pk):
        book = self.get_book_by_pk(pk)
        book.delete()
        return JsonResponse({'message': 'Book deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
                        


    
