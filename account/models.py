from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from account.managers import AccountManager


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username', max_length=30, unique=True)
    email = models.EmailField('email', unique=True)
    
    first_name = models.CharField('first name', max_length=30)
    last_name = models.CharField('last name', max_length=30)
    biography = models.TextField('biography', max_length=150, blank=True, null=True)

    data_joined = models.DateTimeField('data of joined', default=timezone.now)

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
