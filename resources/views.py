from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Philosopher, Idea, School, Book
from .serializers import (
	IdeaSerializer,
	SchoolSerializer,
	PhilosopherSerializer,
	BookSerializer
)

class BookViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Book.objects.order_by('id')
	serializer_class = BookSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['title']

class PhilosopherViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Philosopher.objects.order_by('id')
	serializer_class = PhilosopherSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['name']

class SchoolViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = School.objects.order_by('id')
	serializer_class = SchoolSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['name']

class IdeaViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Idea.objects.order_by('id')
	serializer_class = IdeaSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['quote']