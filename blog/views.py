from django.shortcuts import render, get_object_or_404
from blog.models import Article,Comment
from blog.forms import CommentForm, CreerArticleForm
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, Http404, HttpResponseRedirect

def accueil(request):
    """
    Affiche les 5 derniers articles du blog. Nous n'avons pas encore
    vu comment faire de la pagination, donc on ne donne pas la
    possibilité de lire les articles plus vieux via l'accueil pour
    le moment.
    """
    articles = Article.objects.filter(is_visible=True).order_by('-date')[:4]

    return render(request, 'blog/accueil.html', {'articles': articles})

def CreerArticle(request):

    """ Une vue pour la création d'un article """

    form = CreerArticleForm(request.POST or None, request.FILES)

    if form.is_valid():

        article = Article()
        article.titre = form.cleaned_data['titre']
        article.categorie = form.cleaned_data['categorie']
        article.pseudo = form.cleaned_data['pseudo']
        article.contenu = form.cleaned_data['contenu']
        article.photo = form.cleaned_data['photo']
        article.save()
        return HttpResponseRedirect(reverse_lazy('accueil'))
    else:
        form = CreerArticleForm()
    return render(request, 'blog/creerarticle.html', {'form':form})

def lire_article(request, id):

    article = Article.objects.get(id=id)
    commentaires = article.comment_list()
    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment = Comment()
        comment.article = article
        comment.pseudo = form.cleaned_data['pseudo']
        comment.email = form.cleaned_data['email']
        comment.contenu = form.cleaned_data['contenu']
        comment.save()
        return redirect ('blog_lire', id=id)
    return render(request, 'blog/lire_article.html', {'article': article, 'form':form})
