from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from account.models import AccountRole, Account
from account.forms import AccountChangeForm, AccountCreationForm


admin.site.unregister(Group)


@admin.register(AccountRole)
class AccountRoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

    fieldsets = (
        (None, {'fields': ('name',)}),
        ('Role permissions', {'fields': (
            'is_create_role',
            'is_update_role',
            'is_assign_role',
            'is_remove_role',
        )}),
        ('Issue permissions', {'fields': (
            'is_update_issue',
            'is_remove_issue',
        )}),
    )

    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Account)
class AccountAdmin(BaseUserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm

    list_display = ('__str__', 'username', 'email',)
    list_filter = ('username', 'first_name', 'last_name', 'email',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'role',)}),
        ('Personal info', {'fields': (
            'first_name',
            'last_name',
            'biography',
        )}),
        ('Permissions', {'fields': (
            'date_joined',
            'is_active',
            'is_banned',
            'is_staff',
            'is_verified',
        )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    search_fields = ('first_name', 'last_name', 'username', 'email')
    ordering = ('id',)
