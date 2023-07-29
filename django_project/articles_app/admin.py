from django.contrib import admin
from .models import Article, Comment


# 1 < ------///  StackedInline view ------ ///>
# class CommentInline(admin.StackedInline):
#     model = Comment
#     extra = 5  # By Default, the fields are 3, but you can add Extras
#
#
# class ArticleAdmin(admin.ModelAdmin):
#     inlines = [
#         CommentInline
#     ]

# 2 < ------///  TabularInline view ------ ///> Preferred

class CommentInline(admin.TabularInline):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
