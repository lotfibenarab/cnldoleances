from django.contrib import admin

from blog.models import Article, Categorie, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'pseudo', 'categorie', 'date', 'is_visible', )
    list_filter = ('categorie', )
    search_fields = ('title', 'pseudo', )

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pseudo', 'email', 'contenu', 'date', 'is_visible', 'article' )
    list_filter = ('pseudo', 'article' )
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields = ('pseudo', )

admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie)
admin.site.register(Comment, CommentAdmin)
