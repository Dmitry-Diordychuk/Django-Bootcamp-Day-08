=====
gallery
=====

gallery is a Django app wich bring the page with imagies gallery uploaded by users.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "gallery" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'gallery',
    ]

2. Include the gallery URLconf in your project urls.py like this::

    path('gallery/', include('gallery.urls')),

3. Run ``python manage.py migrate`` to create the gallery models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/ to see the gallery.
