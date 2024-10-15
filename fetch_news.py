import requests
import os
from news.models import Article
from dotenv import load_dotenv
load_dotenv()

API_KEY = str(os.getenv('API_KEY_1'))
URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=' + API_KEY

def fetch_news():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        for item in articles:
            title = item['title']
            content = item['description']
            published_date = item['publishedAt'][:10]  # Extract date in YYYY-MM-DD format

            # Create and save the article in the database
            Article.objects.get_or_create(
                title=title,
                content=content,
                published_date=published_date
            )

# Run this script in Django shell
# python manage.py shell
# >>> from your_script_file import fetch_news
# >>> fetch_news()
