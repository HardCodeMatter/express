from django.shortcuts import render, HttpResponse
from account.models import Account


def account_list_view(request: HttpResponse) -> HttpResponse:
    accounts: Account = Account.objects.all()

    context = {
        'accounts': accounts,
    }

    return render(request, 'account/account_list.html', context)
