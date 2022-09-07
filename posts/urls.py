from django.urls import path, include
from posts import views

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
<<<<<<< HEAD
    path('', views.PostList.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
=======
    path('', views.PostList.as_view(), name = 'PostList'),

    

>>>>>>> 6dce91ecb4446d8b2594226e8c03fce84d43c8b7
]