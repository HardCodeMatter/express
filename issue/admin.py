from django.contrib import admin

from issue.models import Tag, Issue


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'author',)
    list_filter = ('name', 'author',)

    fieldsets = (
        ('None', {'fields': ('name', 'author',)}),
    )

    search_fields = ('name', 'author',)
    ordering = ('-id',)


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
        ('Tags', {'fields': (
            'tags',
        )}),
    )

    search_fields = ('title', 'subtitle', 'writer', 'date_published',)
    ordering = ('-id',)
