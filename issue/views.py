from django.shortcuts import render, HttpResponse
from issue.models import Issue


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
