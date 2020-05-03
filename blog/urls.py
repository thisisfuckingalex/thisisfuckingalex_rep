from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('categories/', views.CategoryList.as_view(), name='category_list'),
    path('<slug:category_slug>/<str:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<slug:category_slug>/', views.CategoryDetail.as_view(), name='category_detail'),
    path('', views.MainView.as_view(), name='main_list')
]