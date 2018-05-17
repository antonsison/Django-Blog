from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Tag


class PostAdmin(admin.ModelAdmin):
	list_display = ["title", "created", "updated"]
	list_display_links = ["updated"]
	list_filter = ["created", "updated"]
	list_editable = ["title"]
	search_fields = ["title", "content"]



admin.site.register(Post, PostAdmin)
admin.site.register(Tag)