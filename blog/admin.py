from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ["author__username", "title", "published_at"]
    raw_id_fields = ['likes']


class TagAdmin(admin.ModelAdmin):
    raw_id_fields = ["posts"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["author__username", "text", "published_at"]
    raw_id_fields = ['post', "author"]


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
