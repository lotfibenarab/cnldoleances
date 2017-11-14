from django.conf.urls import  url
from . import views

urlpatterns = [

    url(r'^$',views.accueil, name='accueil'),
    url(r'^Detail/(?P<id>\d+)$', views.lire_article, name='blog_lire'),
    url(r'^CreerDoleance/$', views.CreerArticle, name='creerarticle'),

]
