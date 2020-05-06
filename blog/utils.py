from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .forms import CommentForm


class PostFilterMixin:
    model = None
    template_name = None

    def get(self, request, category_slug):
        post = self.model.objects.filter(to_display=True, category__slug=category_slug)
        print(category_slug)
        print(post)
        return render(request, self.template_name, {'category_detail': post})


class CountVisitMixin:
    model = None
    template_name = None

    def get(self, request):
        main = self.model.objects.all()
        template = self.template_name
        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits+1
        return render(request, template, context={'main': main, 'num_visits': num_visits})


# class SuggestedPostFilterMixin:
#     model = None
#     template_name = None
#
#     def get(self, request, category_slug):
#         post = self.model.objects.filter(to_display=False, category__slug=category_slug)
#         return render(request, self.template_name, {'suggested_category_detail': post})
#
#
# class SuggestedPostDetailMixin:
#
#     model = None
#     template_name = None
#
#     def get_queryset(self):
#         return self.model.objects.filter(to_display=True)
#
#     def get(self, request, **kwargs):
#         post = get_object_or_404(self.get_queryset(), slug=kwargs.get('post_slug'))
#         return render(request, self.template_name,
#                       {'sug_post': post}
#         )








