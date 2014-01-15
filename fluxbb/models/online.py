from django.db import models
from fluxbb import FLUXBB_PREFIX
from .fluxbb_fields import UnixTimestampField


class Online(models.Model):
    """
    FluxBB Online

    Fields on this model match exactly with those defined by fluxbb, see the
    [fluxbb dbstructure](http://fluxbb.org/docs/v1.5/dbstructure#users).
    """
    user = models.ForeignKey('fluxbb.FluxBBUser', db_constraint=False)
    ident = models.CharField(max_length=200, primary_key=True, unique=True)
    logged = UnixTimestampField(auto_now_add=True)
    idle = models.BooleanField()
    last_post = UnixTimestampField(blank=True, null=True, default=None)
    last_search = UnixTimestampField(blank=True, null=True, default=None)

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'online'
