"""
:mod:`fluxbb.auth` --- FluxBB Authentication Utilities
======================================================

.. module:: fluxbb
    :synopsis: p

This module provides tools for using :mod:`fluxbb` as an authentication backend
and user model.
"""
from django.contrib.auth import get_user_model
from fluxbb.functions import authenticate_user
from fluxbb.models import FluxBBUser

if get_user_model() is FluxBBUser:
    _useratt = 'user'
else:
    _useratt = 'fluxbb_user'


def authenticate(username=None, password=None):
    """Authenticate a user

    Attempts to find and return a FluxBB user matching the provided username
    and password.

    Args:
        username (str): The username
        password (str): The raw password

    Returns:
        If a matching user is found, the ``fluxbb.Users`` instance is returned.
        Otherwise ``None`` is returned.
    """
    try:
        user = FluxBBUser.objects.get(username=username)
        if authenticate_user(user, password):
            return user
    except FluxBBUser.DoesNotExist:
        pass
    return None


def login(request, user):
    """Login a user using FluxBB session management

    Logs the user in on a given request. This sets the appropriate user
    attribute on the request. If ``AUTH_USER_MODEL = "fluxbb.Users"`` is set,
    this will set ``request.user``. Otherwise it will set
    ``request.fluxbb_user``.

    FluxBB uses cookie only session management, and this function will not
    set the cookie. For the login to persist across views, the
    ``fluxbb.auth.middleware.FluxBBSessionManager`` middleware must be active.

    Args:
        request: The HttpRequest to attach to
        user: The fluxbb.Users instance to login
    """
    setattr(request, _useratt, user)
