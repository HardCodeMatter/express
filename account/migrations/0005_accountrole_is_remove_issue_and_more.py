# Generated by Django 4.2.4 on 2023-08-07 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_accountrole_is_remove_role_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountrole',
            name='is_remove_issue',
            field=models.BooleanField(blank=True, default=False, verbose_name='Remove issue'),
        ),
        migrations.AddField(
            model_name='accountrole',
            name='is_update_issue',
            field=models.BooleanField(blank=True, default=False, verbose_name='Update issue'),
        ),
    ]
