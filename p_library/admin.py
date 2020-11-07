from django.contrib import admin

from p_library.models import Author, Book, Redaction


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name', 'ISBN', 'redaction',)
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'copy_count', 'redaction',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    @staticmethod
    def name(obj):
        return obj.full_name

    list_display = ('name', 'birth_year', 'country',)


@admin.register(Redaction)
class RedactionAdmin(admin.ModelAdmin):
    pass
