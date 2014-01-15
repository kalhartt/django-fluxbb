from django.db import models
from fluxbb import FLUXBB_PREFIX
from .fluxbb_fields import UnixTimestampField
_null = {'blank': True, 'null': True, 'default': None}


class Ban(models.Model):
    """
    FluxBB Ban

    Model Fields:
        id (int): Auto incrementing primary key for the model
        username (str): Name of banned user, or None
        ip (str): IP address/mask of banned user, or None
        email (str): Email address of banned user, or None
        message (str): Message to display to the banned user, or None
        expire (datetime): Time at which the ban expires
        ban_creator (FluxBBUser): User who created the ban
    """
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, **_null)
    ip = models.CharField(max_length=255, **_null)
    email = models.CharField(max_length=80, **_null)
    message = models.CharField(max_length=255, **_null)
    expire = UnixTimestampField(**_null)
    ban_creator = models.ForeignKey(
        'fluxbb.FluxBBUser', db_column='ban_creator', db_constraint=False)

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'bans'
