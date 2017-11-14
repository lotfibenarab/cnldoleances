from django import forms
from blog.models import Comment, Article

class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment
        def clean(self):
            cleaned_data = super(ContactForm, self).clean()
        fields = ('pseudo', 'email', 'contenu')

class CreerArticleForm(forms.ModelForm):

    class Meta:

        model = Article

        fields = ('titre','categorie','pseudo','contenu','photo')

    def __init__(self, *args, **kwargs):
        super(CreerArticleForm, self).__init__(*args, **kwargs)
        self.fields['titre'].widget.attrs.update({'class' : 'form-control' })
        self.fields['categorie'].widget.attrs.update({'class' : 'form-control' })
        self.fields['pseudo'].widget.attrs.update({'class' : 'form-control' })
        self.fields['contenu'].widget.attrs.update({'class' : 'form-control' })
        self.fields['photo'].widget.attrs.update({'class' : 'form-control' })
