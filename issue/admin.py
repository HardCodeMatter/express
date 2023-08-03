from django.contrib import admin

from issue.models import Issue


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'writer', 'date_published',)
    list_filter = ('id', 'writer', 'date_published',)

    fieldsets = (
        (None, {'fields': ('title', 'subtitle', 'date_published',)}),
        ('Content', {'fields': (
            'content',
            'image',
        )}),
        ('Publishment', {'fields': (
            'writer',
        )}),
    )

    search_fields = ('title', 'subtitle', 'writer', 'date_published',)
    ordering = ('-id',)
