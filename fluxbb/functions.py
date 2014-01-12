"""Contains authentication functions found in FluxBB's functions.php"""
import hashlib
import hmac
import re
import time
from fluxbb import FLUXBB_COOKIE_SEED, FLUXBB_COOKIE_NAME, pun_config
from fluxbb.models import Users

_COOKIE_RE = re.compile(r'(?P<user_id>\d+)%7C'
                        r'(?P<password_hash>[0-9a-fA-F]+)%7C'
                        r'(?P<expiration_time>\d+)'
                        r'(?P<cookie_hash>[0-9a-fA-F]+)')


def check_cookie(cookie):
    """Validate a FluxBB Authentication cookie

    Args:
        cookie (str): Value of the FluxBB cookie acquired from
            ``request.COOKIES[FLUXBB_COOKIE_NAME]``.

    Returns:
        fluxbb.Users model intance of the user if the cookie succesfully
        authenticated, otherwise it returns ``None``.
    """
    try:
        # parse the cookie string
        cookie = _COOKIE_RE.match(cookie).groupdict()
        user = Users.objects.get(pk=int(cookie['user_id']))
        expiration = int(cookie['expiration_time'])
    except (AttributeError, KeyError, Users.DoesNotExist):
        # cookie not set or invalid
        return None

    now = time.time()
    if user.id > 1 and expiration > now:
        # Validate cookie hash
        cookie_hash = forum_hmac(
            '{0}|{1}'.format(user.id, expiration),
            FLUXBB_COOKIE_SEED + '_cookie_hash')
        if cookie_hash != cookie['cookie_hash']:
            return None

        # Validate password hash
        password_hash = forum_hmac(
            user.password,
            FLUXBB_COOKIE_SEED + '_password_hash')
        if password_hash != cookie['password_hash']:
            return None

        return user
    return None


def authenticate_user(user, password, password_is_hash=False):
    """Authenticate a user

    Args:
        user (str): Users instance of the user to authenticate
        password (str): Password (or password hash) to verify
        password_is_hash (bool): (Optional) If true, password is assumed to
            already be hashed. Defaults to ``False``.

    Returns:
        True if the password authenticates the user, False otherwise. An
        attempt to authenticate the "Guest" user will always return False.
    """
    if user.id == 1:
        # Guest user
        return False

    if password_is_hash:
        return password == user.password
    else:
        return pun_hash(password) == user.password


def forum_hmac(data, key, raw_output=False):
    """Generate keyed hash value using HMAC with sha1

    Args:
        data (str): Data to hash
        key (str): Shared secret key to generate the digest with
        raw_output (bool): (Optional) If ``True``, the digest will be generated
            as a binary string. Otherwise, the hexdigest is returned.

    Returns:
        Returns a string containing the calculated message digest.
    """
    h = hmac.new(key, data, hashlib.sha1)
    if raw_output:
        return h.digest()
    else:
        return h.hexdigest()


def pun_setcookie(response, user_id, password, expire):
    """Wrapper around forum_setcookie."""
    # TODO
    password_hash = forum_hmac(password, FLUXBB_COOKIE_SEED + '_password_hash')
    cookie_hash = forum_hmac('{0}|{1}'.format(user_id, expire),
                             FLUXBB_COOKIE_SEED + '_cookie_hash')
    forum_setcookie(
        response,
        FLUXBB_COOKIE_NAME,
        '{0}|{1}|{2}|{3}'.format(user_id, password_hash, expire, cookie_hash),
        expire)


def forum_setcookie(response, name, value, expire):
    # TODO
    if expire - time.time() - pun_config('o_timeout_visit', cast=int) < 1:
        expire = 0
    response.set_cookie()


def check_username(username, exclude_id=None):
    pass


def pun_hash(msg):
    return hashlib.sha1(msg).hexdigest()
