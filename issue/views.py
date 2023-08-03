from django.shortcuts import render, HttpResponse
from issue.models import Issue


def issue_list_view(request: HttpResponse) -> HttpResponse:
    issues: Issue = Issue.objects.all()

    context = {
        'issues': issues,
    }

    return render(request, 'issue/issue_list.html', context)
