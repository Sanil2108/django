from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView

from app1.models import Article, User

class MyView1(TemplateView):
    def get(self, request):
        return render(request, 'template1.html', context = {'someNumber': 1, 'someArray': [1, 2, 3, 4, 5, 6]})

class MyView2(TemplateView):
    template_name = 'template2.html'

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class UserListView(ListView):
    model = User
    template_name = 'users_list.html'
    context_object_name = 'users_list'

class UserCreate(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'age', 'email']

