from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Main(models.Model):
    greeting = models.CharField('Greeting', max_length=100)
    about_pr = models.TextField('About project', max_length=1000)


class Category(models.Model):
    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('Url', max_length=100, unique=True)
    description = models.CharField('Description', max_length=200)
    template = models.CharField('Template', default='blog_t/category_list.html', max_length=500)
    to_display = models.BooleanField('To display?', default=True)
    sort = models.PositiveIntegerField('Sort', default=0)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Author',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField('Title', max_length=100)
    slug = models.SlugField('Url', max_length=100, unique=True)
    description = models.TextField('Description', max_length=400)
    text = models.TextField('Text')
    category = models.ForeignKey(
        Category,
        verbose_name="Category",
        on_delete=models.CASCADE,
        null=True
    )
    created_date = models.DateTimeField("Created_date", auto_now_add=True)
    edit_date = models.DateTimeField(
        "Edit date",
        default=timezone.now,
        blank=True,
        null=True
    )
    # published_date = models.DateTimeField(
    #     "Published date",
    #     default=timezone.now,
    #     blank=True,
    #     null=True
    # )
    template = models.CharField("template", max_length=500, default="blog_t/post_detail.html")
    to_display = models.BooleanField('To display?', default=True)
    for_auth = models.BooleanField('For authorized?', default=False)
    sort = models.PositiveIntegerField('Sort', default=0)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ["sort", "-created_date"]

    def get_comments_count(self):
        return self.comments.count()

    def get_category_template(self):
        return self.category.template

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'category': self.category.slug, 'slug': self.slug})

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Модель комментария поста"""
    author = models.ForeignKey(
        User,
        verbose_name="Author",
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        verbose_name="Article",
        on_delete=models.CASCADE,
        related_name="comments"
    )
    text = models.TextField("Комментарий")
    created_date = models.DateTimeField("Created date", auto_now_add=True, null=True)
    moderation = models.BooleanField(default=True)

    class Meta:
        ordering = ('created_date', )