# Generated by Django 4.2.4 on 2023-08-16 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_accountrole_is_remove_issue_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountrole',
            name='is_assign_role',
        ),
        migrations.RemoveField(
            model_name='accountrole',
            name='is_create_role',
        ),
        migrations.RemoveField(
            model_name='accountrole',
            name='is_remove_issue',
        ),
        migrations.RemoveField(
            model_name='accountrole',
            name='is_remove_role',
        ),
        migrations.RemoveField(
            model_name='accountrole',
            name='is_update_issue',
        ),
        migrations.RemoveField(
            model_name='accountrole',
            name='is_update_role',
        ),
    ]
