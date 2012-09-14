from django.conf import settings
from django.db.models import get_model

DEFAULT_SETTINGS = {
    'ADMIN_FIELDS': {},
    'INLINE_FIELDS': {},
}

USER_SETTINGS = DEFAULT_SETTINGS.copy()
USER_SETTINGS.update(getattr(settings, 'TINYMCEWRAPPER_SETTINGS'))

admin_fields = {}
for model_str, fields in USER_SETTINGS['ADMIN_FIELDS'].items():
    admin_fields[get_model(*model_str.split('.'))] = fields
USER_SETTINGS['ADMIN_FIELDS'] = admin_fields

globals().update(USER_SETTINGS)
