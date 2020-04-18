from django.contrib import admin
from django.urls import path, include

from app1.views import MyView1, MyView2, ArticleListView, UserListView, UserCreate

urlpatterns = [
    path('', MyView1.as_view()),
    path('view2/', MyView2.as_view()),
    path('articleList/', ArticleListView.as_view()),
    path('usersList/', UserListView.as_view()),
    path('usersCreate/', UserCreate.as_view()),
]
