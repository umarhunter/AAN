from django.shortcuts import render, get_object_or_404, redirect
from .models import Section, Thread, Post
from django.contrib.auth.decorators import login_required

def forum_home(request):
    sections = Section.objects.all()
    return render(request, 'forum/forum_home.html', {'sections': sections})

def section_threads(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    threads = section.threads.all()
    return render(request, 'forum/section_threads.html', {'section': section, 'threads': threads})

def thread_posts(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    posts = thread.posts.all()
    return render(request, 'forum/thread_posts.html', {'thread': thread, 'posts': posts})

@login_required
def create_thread(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            thread = Thread.objects.create(
                section=section,
                title=title,
                created_by=request.user
            )
            return redirect('thread_posts', thread_id=thread.id)
    return render(request, 'forum/create_thread.html', {'section': section})

@login_required
def create_post(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Post.objects.create(
                thread=thread,
                content=content,
                created_by=request.user
            )
            return redirect('thread_posts', thread_id=thread.id)
    return render(request, 'forum/create_post.html', {'thread': thread})
