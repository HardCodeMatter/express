from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from account.models import Account


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('email',)


class AccountChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ('email',)
