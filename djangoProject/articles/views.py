from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView, UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'

class ArticleEditView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    fields = ("title", "body")
    template_name = "articles/article_edit.html"
    success_url = reverse_lazy('article_list')
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author

class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    template_name = "articles/article_delete.html"
    success_url = reverse_lazy('article_list')
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author

class ArticleCreateView(LoginRequiredMixin , CreateView):
    model = Article
    fields = ("title", "body")
    template_name = "articles/article_create.html"
    success_url = reverse_lazy('article_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)