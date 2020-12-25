from django.db import models
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def recount_likes(self):
        self.likes = self.profiles.count()
        self.save()


# Не могу понять почему не работает null=True для полей с датой
class Profile(models.Model):
    liked_posts = models.ManyToManyField(
        'Post', related_name='profiles', blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    last_login = models.DateTimeField(default=timezone.now())
    last_request = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'Доп. инфа для пользователя {self.user.username}'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, **kwargs):
    created = kwargs.get('created')
    last_login = timezone.now()
    if instance.last_login:
        last_login = instance.last_login
    if created:
        profile = Profile.objects.create(
            user=instance, last_login=last_login)
        profile.save()
