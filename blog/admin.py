from django.contrib import admin

from blog.models import Comment, Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ["author__username", "title", "published_at"]
    raw_id_fields = ['likes']


class CommentAdmin(admin.ModelAdmin):
    list_display = ["author__username", "text", "published_at"]
    raw_id_fields = ['post', "author"]


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
