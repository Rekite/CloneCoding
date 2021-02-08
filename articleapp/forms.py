from django import forms
from django.forms import ModelForm

from articleapp.models import Article

from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    # wysiwyg 텍스트 필드를 커스텀
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto;'}))
    # 프로젝트를 꼭 선택하지 않아도 되게
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']