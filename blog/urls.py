from django.urls import path

from . import views

urlpatterns = [
    # path('suggested/', views.SuggestedCategoryList.as_view(), name='suggested_category_list'),
    # path('suggested/<slug:category_slug>/<slug:post_slug>/', views.SuggestedPostDetail.as_view(),
    #      name='suggested_posts_detail'),
    # path('suggested/<slug:category_slug>/', views.SuggestedCategoryDetail.as_view(), name='suggested_posts'),

    path('post-creation/', views.PostCreate.as_view(), name='post_creation'),
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('categories/', views.CategoryList.as_view(), name='category_list'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('<slug:category_slug>/<post_slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<slug:category_slug>/', views.CategoryDetail.as_view(), name='category_detail'),

    path('', views.MainView.as_view(), name='main_list')
]