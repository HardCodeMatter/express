from django.shortcuts import render, redirect, HttpResponse

from issue.models import Issue, Tag
from issue.forms import IssueForm, TagForm


def issue_list_view(request: HttpResponse) -> HttpResponse:
    issues: Issue = Issue.objects.all()

    context = {
        'issues': issues,
    }

    return render(request, 'issue/issue_list.html', context)

def issue_detail_view(request: HttpResponse, id: int) -> HttpResponse:
    issue: Issue = Issue.objects.get(id=id)

    context = {
        'issue': issue,
    }

    return render(request, 'issue/issue_detail.html', context)

def issue_create_view(request: HttpResponse) -> HttpResponse:
    if request.method == 'POST':
        form = IssueForm(request.POST, request.FILES)

        if form.is_valid():
            issue = Issue.objects.create(
                title=form.cleaned_data['title'],
                subtitle=form.cleaned_data['subtitle'],
                content=form.cleaned_data['content'],
                image=form.cleaned_data['image'],
                writer=request.user,
            )

            return redirect(f'/issue/{issue.id}/')
    else:
        form = IssueForm()

    context = {
        'form': form,
    }

    return render(request, 'issue/issue_create.html', context)


def tag_create_view(request: HttpResponse) -> HttpResponse:
    if request.method == 'POST':
        form = TagForm(request.POST)

        if form.is_valid():
            Tag.objects.create(
                name=form.cleaned_data['name'],
                author=request.user,
            )

            return redirect(f'/issue/tags/')
    else:
        form = TagForm()

    context = {
        'form': form,
    }

    return render(request, 'issue/tag_create.html', context)
