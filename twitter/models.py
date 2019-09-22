from django.contrib.auth.models import User
from django.db import models


class Tweet(models.Model):
    content = models.CharField(max_length=255, verbose_name='treść')
    creation_date = models.DateTimeField(auto_now=True, verbose_name='data')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='użytkownik')

    def __str__(self):
        return f'({self.creation_date}) {self.owner}: {self.content[:20]}'
