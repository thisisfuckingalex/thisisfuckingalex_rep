from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, View, DetailView

from .models import Main, Category, Post
from .utils import PostFilterMixin, CountVisitMixin
from .forms import CommentForm


class MainView(CountVisitMixin, ListView):
    model = Main
    template_name = 'blog_t/main.html'


class CategoryList(ListView):
    """Вывод всех статей для category_list.html"""
    model = Category
    template_name = 'blog_t/category_list.html'

    def get_queryset(self):
        return self.model.objects.filter(to_display=True)


class CategoryDetail(PostFilterMixin, ListView):
    """Вывод постов категории"""
    model = Post
    template_name = 'blog_t/category_detail.html'


class PostList(ListView):
    """Вывод всех постов"""
    model = Post
    template_name = 'blog_t/post_list.html'


class PostDetailView(View):
    """Вывод полной статьи"""

    def get(self, request, **kwargs):
        post = get_object_or_404(Post, slug=kwargs.get("slug"))
        form = CommentForm()
        return render(request, post.template,
                      {'post': post, 'form': form}
        )

    def post(self, request, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = Post.objects.get(slug=kwargs.get('slug'))
            form.author = request.user
            form.save()
        return redirect(request.path)
