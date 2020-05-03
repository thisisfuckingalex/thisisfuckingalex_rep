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
        return render(request, self.template_name, context={'category_detail': post})


class CountVisitMixin:
    model = None
    template_name = None

    def get(self, request):
        main = self.model.objects.all()
        template = self.template_name
        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits+1
        return render(request, template, context={'main': main, 'num_visits': num_visits})
