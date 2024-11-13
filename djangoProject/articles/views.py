from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView, UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic.edit import FormMixin
from django.forms import forms
from .forms import CommentForm



# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'

class ArticleDetailView(FormMixin,DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    form_class = CommentForm
    def get_success_url(self):
        return reverse_lazy('article_detail',kwargs={'pk':self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'article':self.object,'writer':self.request.user})
        return context

    def post(self, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            pass

    def form_valid(self, form):
        form.save()
        return super(ArticleDetailView, self).form_valid(form)

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



