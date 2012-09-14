from django.contrib import admin

from .models import SimpleModel, InlineModel


class SimpleInline(admin.TabularInline):
    model = InlineModel


class SimpleModelAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    inlines = [SimpleInline]

admin.site.register(SimpleModel, SimpleModelAdmin)
