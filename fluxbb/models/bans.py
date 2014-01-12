from django.db import models
from fluxbb import FLUXBB_PREFIX
from fluxbb_fields import UnixTimestampField

_null = {'blank': True, 'null': True, 'default': None}


class Bans(models.Model):
    """
    FluxBB Bans

    Fields on this model match exactly with those defined by fluxbb, see the
    [fluxbb dbstructure](http://fluxbb.org/docs/v1.5/dbstructure#users).
    """
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, **_null)
    ip = models.CharField(max_length=255, **_null)
    email = models.CharField(max_length=80, **_null)
    message = models.CharField(max_length=255, **_null)
    expire = UnixTimestampField(**_null)
    ban_creator = models.ForeignKey('fluxbb.Users', db_column='ban_creator',
                                    db_constraint=False)

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'bans'
