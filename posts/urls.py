from django.urls import path, include
from posts import views

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view(), name = 'PostList'),

    

]