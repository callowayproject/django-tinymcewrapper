=================================
Django TinyMCEWrapper v |version|
=================================

About
=====

We created Django TinyMCEWrapper to allow us to enable a TinyMCE widget on various third-party Django apps' ModelAdmin, without having to fork the apps or re-do their ModelAdmin.

The process is flexible, simple and harmless. Django-TinyMCEWrapper redefines the ModelAdmin class after all admin classes are registered and overrides the widget used for the configured fields.

Contents
========

.. toctree::
   :maxdepth: 2
   :glob:
   
   installation
   getting_started
   configuration
   reference/index
