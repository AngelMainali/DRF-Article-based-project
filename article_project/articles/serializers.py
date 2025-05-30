from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Article

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['is_staff', 'is_superuser']
    def create(self, validated_data):
        user= User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )    
        return user
    
class ArticleSerializer(serializers.ModelSerializer):
    author=serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),write_only=True)
    authors_details = UserDetailsSerializer(source='author',read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'