django-fluxbb
=============

Django application for interfacing with a fluxbb board

installation
============

Add `fluxbb` to the `INSTALLED_APPS` section of your settings.py.
It is recommended to install fluxbb with a table prefix to avoid potential
naming collisions. For django-fluxbb to recognize the prefix, add this setting
to your settings.py (replace `fluxbb_` with the prefix you specified.

```
FLUXBB_PREFIX = 'fluxbb_'
```

Using a separate database for fluxbb
====================================
A simple router is included if you are using a separate database for the
fluxbb instance. Simply define a database named `fluxbb` and use the included
router.

```
DATABASES = {
    ...
    'fluxbb': {
        'ENGINE': ...
    }
}

DATABASE_ROUTERS = ['fluxbb.routers.FluxBBRouter', ...]
```
