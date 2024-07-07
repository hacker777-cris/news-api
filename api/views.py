from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer
from django.shortcuts import get_object_or_404


class AllArticles(APIView):
    def get(self, request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        data = serializer.data
        return Response({"success": True, "data": data})


class SingleArticle(APIView):
    def get(self, request):
        title = request.query_params.get("title")
        try:
            article = get_object_or_404(Article, title=title)
            serializer = ArticleSerializer(article)
            data = serializer.data
            return Response({"success": True, "data": data})
        except Exception as e:
            return Response(
                {"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )
