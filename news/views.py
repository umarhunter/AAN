import requests
import os

from django.shortcuts import render
from decouple import config
from .models import Article


def fetch_news():
    API_KEY = config('API_KEY_1')
    URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=' + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        for item in articles:
            title = item['title']
            content = item['description'] or 'No description available'  # Handle missing content
            published_date = item['publishedAt'][:10]  # Extract date in YYYY-MM-DD format

            # Create and save the article in the database
            Article.objects.get_or_create(
                title=title,
                content=content,
                published_date=published_date
            )


def home(request):
    fetch_news()
    articles = Article.objects.order_by('-published_date')
    return render(request, 'news/home.html', {'articles': articles})

def about(request):
    return render(request, 'news/about.html')

def contact(request):
    return render(request, 'news/contact.html')