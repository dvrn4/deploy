from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Notebook
from .serializers import NotebookSerializer

# Generics: List va Delete (Delete bir item uchun)
class NotebookListAPIView(generics.ListAPIView):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer

class NotebookDeleteAPIView(generics.DestroyAPIView):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer

# APIView-lardan voris olgan Create
class NotebookCreateAPIView(APIView):
    def post(self, request):
        serializer = NotebookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# APIView: Detail (GET)
class NotebookDetailAPIView(APIView):
    def get(self, request, pk):
        notebook = get_object_or_404(Notebook, pk=pk)
        serializer = NotebookSerializer(notebook)
        return Response(serializer.data)

# APIView: Update (PUT va PATCH)
class NotebookUpdateAPIView(APIView):
    def put(self, request, pk):
        notebook = get_object_or_404(Notebook, pk=pk)
        serializer = NotebookSerializer(notebook, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        notebook = get_object_or_404(Notebook, pk=pk)
        serializer = NotebookSerializer(notebook, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# APIView: DeleteUpdateDetail - bitta klassda get/put/patch/delete
class NotebookDeleteUpdateDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Notebook, pk=pk)

    def get(self, request, pk):
        nb = self.get_object(pk)
        serializer = NotebookSerializer(nb)
        return Response(serializer.data)

    def put(self, request, pk):
        nb = self.get_object(pk)
        serializer = NotebookSerializer(nb, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        nb = self.get_object(pk)
        serializer = NotebookSerializer(nb, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        nb = self.get_object(pk)
        nb.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
