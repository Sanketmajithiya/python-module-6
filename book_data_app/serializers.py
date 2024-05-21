from rest_framework import serializers
from .models import Books

class BlogsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['title', 'author', 'isbn', 'publisher']