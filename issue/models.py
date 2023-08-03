from django.db import models
from django.utils import timezone

from account.models import Account


class Issue(models.Model):
    title = models.CharField('title', max_length=100)
    subtitle = models.CharField('subtitle', max_length=100, blank=True, null=True)
    content = models.TextField('content', max_length=5000)

    image = models.ImageField('image', upload_to='issue/image/', blank=True, null=True)

    writer = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_published = models.DateField('date of published', default=timezone.now)


    def __str__(self):
        return f'Issue {self.pk}'
    

    class Meta:
        verbose_name = 'Issue'
        verbose_name_plural = 'Issues'
