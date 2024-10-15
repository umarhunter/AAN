from django.shortcuts import render
from .models import Article

def home(request):
    articles = Article.objects.order_by('-published_date')
    return render(request, 'news/home.html', {'articles': articles})

def about(request):
    return render(request, 'news/about.html')

def contact(request):
    return render(request, 'news/contact.html')