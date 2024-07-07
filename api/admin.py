from django.contrib import admin
from .models import Article

Article = admin.site.register(Article)
