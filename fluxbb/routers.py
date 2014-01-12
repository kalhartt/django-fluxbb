"""
Module providing a router to handle a separate fluxbb database
"""


class FluxBBRouter(object):
    """
    Router to move all fluxbb queries to the appropriate database
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'fluxbb':
            return 'fluxbb'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'fluxbb':
            return 'fluxbb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if any(o._meta.app_label == 'fluxbb' for o in (obj1, obj2)):
            return True
        return False

    def allow_syncdb(self, db, model):
        return None
