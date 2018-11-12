from django.contrib import admin



from articles.models import Article, Vote, Comment

admin.site.register(Article)
admin.site.register(Vote)
admin.site.register(Comment)