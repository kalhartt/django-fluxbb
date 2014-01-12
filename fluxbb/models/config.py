from django.db import models
from fluxbb import FLUXBB_PREFIX


class Config(models.Model):
    """
    FluxBB Config

    Fields on this model match exactly with those defined by fluxbb, see the
    [fluxbb dbstructure](http://fluxbb.org/docs/v1.5/dbstructure#users).
    """
    conf_name = models.CharField(max_length=255, default="")
    conf_value = models.TextField(blank=True, null=True, default=None)

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'config'
