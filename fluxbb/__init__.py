"""
Package for django integration with fluxbb forum
"""
from django.conf import settings

# The table prefix used by the models
FLUXBB_PREFIX = getattr(settings, 'FLUXBB_PREFIX', '')
FLUXBB_COMPOSITEKEYFIX = getattr(settings, 'FLUXBB_COMPOSITEKEYFIX', False)
