from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllArticles.as_view()),
    path("get_article/", views.SingleArticle.as_view()),
]
