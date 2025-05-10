from rest_framework import serializers
from .models import Category, Nominee, Vote

class NomineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nominee
        fields = ['id', 'name', 'image_url']

class CategorySerializer(serializers.ModelSerializer):
    nominees = NomineeSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'nominees']

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['nominee', 'ip_address']
