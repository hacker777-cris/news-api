from django.core.management.base import BaseCommand
import requests
from api.models import Article
import os
from dotenv import load_dotenv


class Command(BaseCommand):
    help = "Fetch latest news articles"

    def handle(self, *args, **kwargs):
        # Load environment variables from .env file
        load_dotenv()

        api_key = os.getenv("API_KEY")
        url = "https://newsapi.org/v2/top-headlines"
        params = {
            "apiKey": api_key,
            "country": "us",
        }
        response = requests.get(url, params=params)
        articles = response.json().get("articles", [])

        for article in articles:
            Article.objects.create(
                title=article["title"],
                description=article["description"],
                url=article["url"],
                published_at=article["publishedAt"],
            )
        self.stdout.write(self.style.SUCCESS("Successfully fetched news articles"))
