
from rest_framework import generics,serializers

from django.contrib.auth.models import User
from articles.serializers import UserDetailsSerializer,ArticleSerializer,CustomTokenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class= UserDetailsSerializer

class LoginView(APIView):
    def post(self,request):
        username= request.data['username']
        password= request.data['password']

        try:
            user = User.objects.get(username=username)

        except:
            return Response({'error':'Invalid username'},status=400)
        
        if user.check_password(password):
            return Response({'message':'Login successful'},status=200)
        else:
            return Response({'error':'Invalid credentials'},status=400)
        

class ArticleCreateGetView(generics.ListCreateAPIView):
    authentication_classes=[JWTAuthentication]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CustomTokenView(TokenObtainPairView):
    serializer_class=CustomTokenSerializer
    




   
    
    
