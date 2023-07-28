from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView, CreateView
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


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('articles_list')


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'new_article.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
