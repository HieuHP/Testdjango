from django.contrib import admin
from .models import Post, Comment
# Register your models here.
#class CommentInline(admin.StackedInline):
class CommentInline(admin.TabularInline):
    model = Comment
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date'] #hiển thị thời gian
    list_filter = ['date'] #hiện thị bài viết khoảng thời gian
    search_fields = ['title']
    inlines = [CommentInline]
admin.site.register(Post, PostAdmin)
