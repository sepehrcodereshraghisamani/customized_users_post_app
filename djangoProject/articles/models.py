from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db.models.fields import TextField
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:detail', args=[str(self.pk)])


class Comment(models.Model):
    article = models.ForeignKey(Article,related_name='comments',on_delete=models.CASCADE)
    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment = models.TextField()
    def __str__(self):
        return str(self.writer) + ' - ' + str(self.pk)

    def get_absolute_url(self):
        return reverse('article_list')

