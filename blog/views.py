from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, View, DetailView
from .models import Main, Category, Post
from .utils import PostFilterMixin, CountVisitMixin
from .forms import CommentForm, PostForm


class MainView(CountVisitMixin, ListView):
    model = Main
    template_name = 'blog_t/main.html'


class CategoryList(ListView):
    """Вывод всех статей для category_list.html"""
    model = Category
    template_name = 'blog_t/category_list.html'


class CategoryDetail(PostFilterMixin, ListView):
    """Вывод постов категории"""
    model = Post
    template_name = 'blog_t/category_detail.html'


class PostList(ListView):
    """Вывод всех постов"""
    model = Post
    template_name = 'blog_t/post_list.html'

    def get_queryset(self):
        return self.model.objects.filter(to_display=True)


class PostDetailView(View):
    """Вывод полной статьи"""
    def get_queryset(self):
        return Post.objects.filter(to_display=True)

    def get(self, request, **kwargs):
        post = get_object_or_404(self.get_queryset(), slug=kwargs.get('post_slug'))
        post_form = PostForm()
        form = CommentForm()
        return render(request, post.template,
                      {'post': post, 'form': form, 'post_form': post_form}
        )

    def post(self, request, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = Post.objects.get(slug=kwargs.get('post_slug'))
            form.author = request.user
            form.save()
        return redirect(request.path)


class PostCreate(View):
    def get(self, request):
        post_form = PostForm()
        return render(request, 'blog_t/post_creation.html', {'post_form': post_form})

    def post(self, request):
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form = post_form.save(commit=False)
            post_form.author = request.user
            post_form.save()
        return redirect(request.path)


# class PostEdit(View):
#     def get_queryset(self):
#         return Post.objects.filter(to_display=True)
#
#     def get(self, request, **kwargs):
#         post = get_object_or_404(self.get_queryset(), slug=kwargs.get('post_slug'))
#         post_edit = PostForm()
#         return render(request, 'blog_t/post_edit.html', {'post_edit': post_edit, 'post': post})
#
#     def post(self, request, **kwargs):
#         post_edit = PostForm(request.POST)
#         if post_edit.is_valid():
#             post = post_edit.save(commit=False)
#             post.author = request.user
#             post.edit_date = timezone.now()
#             post.save()
#         else:
#             post_edit = PostForm(instance=post)
#         return redirect('blog_t/post_detail.html', slug=kwargs.get('post_slug'))


def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        edit_form = PostForm(request.POST, instance=post)
        if edit_form.is_valid():
            post = edit_form.save(commit=False)
            post.author = request.user
            post.edit_date = timezone.now()
            post.save()
            return redirect('main_list', )
    else:
        edit_form = PostForm(instance=post)
    return render(request, 'blog_t/post_edit.html', {'edit_form': edit_form})


# class SuggestedCategoryList(ListView):
#
#     model = Category
#     template_name = 'blog_t/suggested_posts/suggested_category_list.html'
#
#
# class SuggestedCategoryDetail(SuggestedPostFilterMixin, View):
#
#     model = Post
#     template_name = 'blog_t/suggested_posts/suggested_category_detail.html'
#
#
# class SuggestedPostDetail(SuggestedPostDetailMixin, View):
#
#     model = Post
#     template_name = 'blog_t/suggested_posts/suggested_post_detail.html'
