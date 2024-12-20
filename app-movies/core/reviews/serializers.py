# We import the libraries
from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField() # Encryption of sensitive data.
    class Meta:
        model = Review
        fields = '__all__'
        depth = 1  # Ratio or depth 1