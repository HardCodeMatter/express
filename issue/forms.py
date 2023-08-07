from django import forms

from issue.models import Issue, Tag


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('title', 'subtitle', 'content', 'image',)


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)
