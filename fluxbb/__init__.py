"""
Package for django integration with fluxbb forum
"""
import time
from django.conf import settings

# The table prefix used by the models
FLUXBB_PREFIX = getattr(settings, 'FLUXBB_PREFIX', '')
FLUXBB_COMPOSITEKEYFIX = getattr(settings, 'FLUXBB_COMPOSITEKEYFIX', False)
FLUXBB_COOKIE_SEED = getattr(settings, 'FLUXBB_COOKIE_SEED', '')
FLUXBB_COOKIE_NAME = getattr(settings, 'FLUXBB_COOKIE_NAME', 'pun_cookie')

_pun_timeout = 10
_pun_config = {}


def pun_config(conf_name, default=None, cast=None):
    """Gets a FluxBB config value

    Looks for a value ``conf_name`` and returns the associated value (casted
    to an appropriate type using ``cast``) if it exists. If the value does not
    exist, it returns ``default``. Values are memoized for 10 seconds to reduce
    database strain in requests.

    Args:
        conf_name (str): Name of the configuration option.
        default: (Optional) Value to return if no match is found,
            Defaults to ``None``
        cast (callable): (Optional) Function to cast the value to an
            appropriate type.

    Returns:
        The configuration value casted using ``cast``. If ``cast`` is not
        given, then the result will be a string.
    """
    # We have to import Config model here to avoid circular imports
    from .models.config import Config

    now = time.time()
    if conf_name in _pun_config:
        value, expire = _pun_config[conf_name]
        if expire < now:
            return value

    try:
        value = Config.objects.get(conf_name=conf_name)
    except Config.DoesNotExist:
        return default

    if cast:
        value = cast(value)

    _pun_config[conf_name] = (value, now + _pun_timeout)
    return value
