from django.contrib import admin
from .models import Articles, Message, Cat
# Register your models here.

admin.site.register(Articles)
admin.site.register(Message)
admin.site.register(Cat)
