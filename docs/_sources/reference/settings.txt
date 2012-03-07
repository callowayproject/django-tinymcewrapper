========
Settings
========

ADMIN_FIELDS
============

ADMIN_FIELDS is a dictionary in the format ``{'app.model': <field configuration>}``. ``<field configuration>`` is either a ``list`` or ``tuple``

.. code-block:: python

   {'app.model': ('field', 'field2',),}

or the ``<field configuration>`` is a ``dict``. 

.. code-block:: python

   {'app.model': {
       'field1': {
           'attrs': {'cols': 80, 'rows': 30},
           'mce_attrs': {'theme': 'advanced'}
       },
       'field2': {} # default configuration
   }}


For more information see :ref:`configuration`.