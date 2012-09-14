from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.core.exceptions import ImproperlyConfigured
from tinymce.widgets import TinyMCE

from .settings import ADMIN_FIELDS


class TinyMCEAdmin(admin.ModelAdmin):
    editor_fields = {}

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(TinyMCEAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in self.editor_fields:
            formfield.widget = TinyMCE(**self.editor_fields[db_field.name])
        return formfield


class TinyMCEInlineAdmin(InlineModelAdmin):
    editor_fields = {}

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(TinyMCEAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in self.editor_fields:
            formfield.widget = TinyMCE(**self.editor_fields[db_field.name])
        return formfield


def get_efields(model):
    """
    Get the editor fields based on the configuration
    """
    if isinstance(ADMIN_FIELDS[model], (list, tuple)):
        return dict([(i, {}) for i in ADMIN_FIELDS[model]])
    elif isinstance(ADMIN_FIELDS[model], dict):
        return ADMIN_FIELDS[model]
    else:
        raise ImproperlyConfigured("The fields for model %s are not a list, tuple or dict." % model.__class__)


for model, modeladmin in admin.site._registry.items():
    inlines = getattr(modeladmin, 'inlines', [])
    for inline in inlines:
        print inline
        if inline.model in ADMIN_FIELDS:
            efields = get_efields(inline.model)
            newinline = type(
                'newadmin', (TinyMCEInlineAdmin, inline), {
                    'editor_fields': efields, })
            inlines[inlines.index(inline)] = newinline
    if model in ADMIN_FIELDS:
        efields = get_efields(model)
        admin.site.unregister(model)
        admin.site.register(model, type('newadmin', (TinyMCEAdmin, modeladmin.__class__), {
            'editor_fields': efields,
        }))
