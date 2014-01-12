import calendar
from datetime import datetime
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UnixTimestampField(models.IntegerField):
    """
    DateTimeField with alternate database storage mechanism.

    DateTimeField which internally stores the time as a UNIX timestamp in an
    integer field. Accepts and returns python datetime.datetime instances, its
    interface is identical to the default django DateTimeField.
    """
    empty_strings_allowerd = False
    default_error_messages = {
        'invalid': _("'%(value)s value must be an integer."),
    }
    description = _("Date (with time)")

    def __init__(self, verbose_name=None, name=None, auto_now=False,
                 auto_now_add=False, **kwargs):
        super(UnixTimestampField, self).__init__(verbose_name, name, **kwargs)

    def get_internal_type(self):
        return "IntegerField"

    def get_prep_value(self, value):
        if value is None:
            return None
        return calendar.timegm(value.timetuple())

    def to_python(self, value):
        value = super(UnixTimestampField, self).to_python(value)
        if value is None:
            return value
        if settings.USE_TZ:
            tz = timezone.get_default_timezone()
            value = datetime.fromtimestamp(value, tz)
        else:
            value = datetime.utcfromtimestamp(value)
