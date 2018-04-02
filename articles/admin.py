from django.contrib import admin



from articles.models import Article, Vote

admin.site.register(Article)
admin.site.register(Vote)