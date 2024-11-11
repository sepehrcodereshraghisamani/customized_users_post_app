from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView, UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'

class ArticleEditView(UpdateView):
    model = Article
    fields = ("title", "body")
    template_name = "articles/article_edit.html"
    success_url = reverse_lazy('article_list')

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "articles/article_delete.html"
    success_url = reverse_lazy('article_list')

class ArticleCreateView(LoginRequiredMixin , CreateView):
    model = Article
    fields = ("title", "body")
    template_name = "articles/article_create.html"
    success_url = reverse_lazy('article_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)