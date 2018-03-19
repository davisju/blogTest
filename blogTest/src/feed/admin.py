from django.contrib import admin
from .models import Ariticle, Comment, HashTag

@admin.register(Ariticle, Comment, HashTag)
class FeedAdmin(admin.ModelAdmin):
    pass
# Register your models here.
