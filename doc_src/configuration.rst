.. _configuration:

=============
Configuration
=============

The ``ADMIN_FIELDS`` setting is a dictionary in the format ``{'app.model': <field configuration>}``. There are two methods to specify *field configuration*: simple and custom.

Simple Configuration
====================

The *field configuration* in the simple configuration is simply a ``tuple`` of strings containing the fields to add a TinyMCE widget in the admin. These fields will use all the defaults for django-tinymce.

.. code-block:: python

   TINYMCEWRAPPER_SETTINGS = {
       'ADMIN_FIELDS': {
           'simpleapp.simplemodel': ('description', 'long_description')
       },
   }

Custom Configuration
====================

For more control over how the TinyMCE widget is rendered, you can use a ``dict`` with the field names as keys and the value a ``dict`` that is passed as keyword arguments to the TinyMCE HTML widget.

.. code-block:: python

   TINYMCEWRAPPER_SETTINGS = {
       'ADMIN_FIELDS': {
          'simpleapp.simplemodel': {
             'description': {
                'attrs': {'cols': 80, 'rows': 30,},
                'mce_attrs': {'theme': 'advanced'}
             },
             'long_description': {},
          }
       },
   }