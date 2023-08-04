from django import forms

from issue.models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('title', 'subtitle', 'content', 'image',)
