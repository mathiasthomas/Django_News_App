from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

# Articles List View\
class ArticlesListView(ListView):
    model = Article
    template_name = 'articles_list.html'


# Detail View

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


# Update View

class ArticleUpdateView(UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = 'articles_update.html'


class ArticleDeleteView(DetailView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('articles_list')
