from django.contrib import admin
from .models import Articles, Message, Cat
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class Articles_admin(SummernoteModelAdmin):
    summernote_fields = ('body',)

admin.site.register(Articles, Articles_admin)
admin.site.register(Message)
admin.site.register(Cat)
