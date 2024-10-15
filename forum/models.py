from django.db import models
from django.contrib.auth.models import User

class Section(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Thread(models.Model):
    section = models.ForeignKey(Section, related_name='threads', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, related_name='threads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    thread = models.ForeignKey(Thread, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post by {self.created_by.username} in {self.thread.title}'
