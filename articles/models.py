from __future__ import unicode_literals

from django.db import models

# Create your models here
class Articles(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank=True)
    img0 = models.ImageField(default='default.png', blank=True)
    img1 = models.ImageField(default = 'default.png',blank=True)
    img2 = models.ImageField(default='default.png', blank=True)
    img3 = models.ImageField(default='default.png', blank=True)
    img4 = models.ImageField(default='default.png', blank=True)
    img5 = models.ImageField(default='default.png', blank=True)
    img6 = models.ImageField(default='default.png', blank=True)
    img7 = models.ImageField(default='default.png', blank=True)
    img8 = models.ImageField(default='default.png', blank=True)
    img9 = models.ImageField(default='default.png', blank=True)


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]

    





