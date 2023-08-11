from django.shortcuts import render
from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
#I'm to create CRUD endpoints. Endpoints that create, read, update and post (submit) data

#read endpoint
class ArticleListView(generics.ListCreateAPIView):
	queryset = Articles.objects.all()
	serializer_class = ArticleSerializer

class ArticleUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Articles.objects.all()
	serializer_class = ArticleSerializer