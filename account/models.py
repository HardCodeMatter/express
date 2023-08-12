from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from account.managers import AccountManager


class AccountRole(models.Model):
    name = models.CharField('name', max_length=30, unique=True)

    is_create_role = models.BooleanField('Create role', blank=True, default=False)
    is_update_role = models.BooleanField('Update role', blank=True, default=False)
    is_assign_role = models.BooleanField('Assign role', blank=True, default=False)
    is_remove_role = models.BooleanField('Remove role', blank=True, default=False)

    is_update_issue = models.BooleanField('Update issue', blank=True, default=False)
    is_remove_issue = models.BooleanField('Remove issue', blank=True, default=False)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Account\'s role'
        verbose_name_plural = 'Account\'s roles'


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username', max_length=30, unique=True)
    email = models.EmailField('email', unique=True)
    
    first_name = models.CharField('first name', max_length=30)
    last_name = models.CharField('last name', max_length=30)
    biography = models.TextField('biography', max_length=150, blank=True, null=True)

    role = models.ForeignKey(AccountRole, on_delete=models.CASCADE, blank=True, null=True, default=None)

    date_joined = models.DateTimeField('date of joined', default=timezone.now)

    is_active = models.BooleanField('active', default=True)
    is_banned = models.BooleanField('banned', default=False)
    is_staff = models.BooleanField('staff', default=False)
    is_verified = models.BooleanField('verified', default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    @property
    def is_administrator(self) -> bool:
        """Is the current user a staff member?"""
        return self.is_staff

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
