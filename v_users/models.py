from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static as static_url  


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user_avatar/', null=True, blank=True)
    realname = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True, null=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(max_length=250, null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.realname or 'Unnamed'}"

    @property
    def avatar_url(self):
        try: 
            avatar_url = self.avatar.url
        except:
            avatar_url = static_url('images/avatar_default.svg')

        return avatar_url       


    @property
    def name(self):
        if self.realname:
            name = self.realname
        else:
            name = self.user.username

        return name        