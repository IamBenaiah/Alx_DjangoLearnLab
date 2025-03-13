from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def book_list(request):
class BookList(ListAPIView):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "API is working!"})

