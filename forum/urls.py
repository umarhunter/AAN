from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_home, name='forum_home'),
    path('section/<int:section_id>/', views.section_threads, name='section_threads'),
    path('thread/<int:thread_id>/', views.thread_posts, name='thread_posts'),
    path('section/<int:section_id>/create_thread/', views.create_thread, name='create_thread'),
    path('thread/<int:thread_id>/create_post/', views.create_post, name='create_post'),
]
