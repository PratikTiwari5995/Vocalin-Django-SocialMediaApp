from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(default='No Title', max_length=500)
    photo = models.ImageField(
        upload_to='post_photo', height_field=None, width_field=None, max_length=None)
    body = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField('Tag')
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4,
                          unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-created']


class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    icon_images = models.FileField(upload_to='icons/', null=True, blank=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='comments')
    parent_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=150)
    created = models.DateField(auto_now_add=True)
    id = models.CharField(
        max_length=100, primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    def __str__(self):
        try:
            return f"{self.author} : {self.body[:30]}"
        except:
            return f"No Author : {self.body[:30]}"

    class Meta:
        ordering = ['-created']


class Reply(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="replies")
    parent_comment = models.ForeignKey(
        Comments, on_delete=models.CASCADE, related_name="replies")
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4,
                          unique=True, primary_key=True, editable=False)

    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}'
        except:
            return f'no author : {self.body[:30]}'

    class Meta:
        ordering = ["created"]
