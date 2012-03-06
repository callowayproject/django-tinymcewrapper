===============
Getting Started
===============

#. Install django-tinymce and django-tinymcewrapper.

#. Configure django-tinymce

#. Configure django-tinymcewrapper:

'ADMIN_FIELDS': {
    'simpleapp.simplemodel': ('description', 'long_description')
},

'ADMIN_FIELDS': {
   'simpleapp.simplemodel': {
      'description': {
         'attrs': {'cols': 80, 'rows': 30,}, 
         'mce_attrs':{'theme': 'advanced'}
      }, 
      'long_description': {},
   }
},

