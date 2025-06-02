from django.urls import path
from .views import RegisterView, LoginView,ArticleCreateGetView,ArticleRetrieveUpdateDestroyView,CustomTokenView

urlpatterns =[

   path('register/',RegisterView.as_view(), name='register-view'),
   path('login/', LoginView.as_view(), name='login-view'),
   path('api/custom-token/',CustomTokenView.as_view(), name='custom-token-view'), 
   path('', ArticleCreateGetView.as_view(), name='article-view'),
   path('<int:pk>/', ArticleRetrieveUpdateDestroyView.as_view(), name='article-view'),

]