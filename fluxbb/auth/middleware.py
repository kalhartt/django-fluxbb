from django.contrib.auth import get_user_model
from fluxbb.models import Users
from fluxbb import FLUXBB_COOKIE_NAME
from fluxbb.functions import check_cookie, pun_setcookie

if get_user_model() is Users:
    _useratt = 'user'
else:
    _useratt = 'fluxbb_user'


class FluxBBSessionMiddleware(object):
    """FluxBB Session Middleware

    Session manager for reading and manipulating the FluxBB authentication
    cookie. If your application uses ``fluxbb.Users`` as its
    ``AUTH_USER_MODEL`` then this will set the ``request.user`` attribute.
    Otherwise it will set the ``request.fluxbb_user`` attribute.
    """

    def process_request(self, request):
        """Process Request

        Attempts to validate a fluxbb user by request and set the ``user`` or
        ``fluxbb_user`` attribute on request. If the user is not authenticated
        the attribute will be set to ``None``.

        Args:
            request: The HttpRequest

        Returns:
            None
        """
        cookie = request.COOKIES.get(FLUXBB_COOKIE_NAME, '')
        setattr(request, _useratt, check_cookie(cookie))

    def process_response(self, request, response):
        """Process Response

        If a fluxbb user is present on the request, we update the user's
        authentication cookie.

        Args:
            request: The HttpRequest
            response: The view generated HttpResponse

        Returns:
            None
        """
        user = getattr(response, _useratt, None)
        if user:
            pun_setcookie(user.id, user.password)
