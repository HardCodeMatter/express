from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from account.models import Account


class RegisterForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)
