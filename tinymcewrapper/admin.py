from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured
from django import forms
from tinymce.widgets import TinyMCE

from .settings import ADMIN_FIELDS


class TinyMCEAdmin(admin.ModelAdmin):
    editor_fields = {}
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in self.editor_fields:
            return db_field.formfield(widget=TinyMCE(**self.editor_fields[db_field.name]))
        return super(TinyMCEAdmin, self).formfield_for_dbfield(db_field, **kwargs)


for model, modeladmin in admin.site._registry.items():
    if model in ADMIN_FIELDS:
        if isinstance(ADMIN_FIELDS[model], (list, tuple)):
            efields = dict([(i, {}) for i in ADMIN_FIELDS[model]])
        elif isinstance(ADMIN_FIELDS[model], dict):
            efields = ADMIN_FIELDS[model]
        else:
            raise ImproperlyConfigured("The fields for model %s are not a list, tuple or dict." % model.__class__)
        admin.site.unregister(model)
        admin.site.register(model, type('newadmin', (TinyMCEAdmin, modeladmin.__class__), {
            'editor_fields': efields,
        }))