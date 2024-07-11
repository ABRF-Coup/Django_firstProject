from django.urls import path
from .views import index_blog,article




urlpatterns = [

    path('',index_blog,name='index-blog'),
    path('article-<str:numero_article>/',article,name='article')
   
]
