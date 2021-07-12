from .models import Philosopher, Idea, School, Book
from rest_framework import serializers

class IdeaSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Idea 
        fields = ['id','quote','author']

class SchoolSerializer(serializers.ModelSerializer):
    philosophers = serializers.StringRelatedField(many=True)

    class Meta:
        model = School 
        fields = ['id','name','philosophers']

class PhilosopherSerializer(serializers.ModelSerializer):
    school = serializers.StringRelatedField(many=True)
    ideas = serializers.StringRelatedField(many=True)
    books = serializers.StringRelatedField(many=True)

    class Meta:
        model = Philosopher 
        fields = [
            'id',
            'name',
            'photo',
            'born_date',
            'death_date',
            'nationality',
            'era',
            'school',
            'ideas',
            'books'
        ]

class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Book 
        fields = [
            'id',
            'title',
            'cover',
            'abstract',
            'country',
            'language',
            'published',
            'author'
        ]