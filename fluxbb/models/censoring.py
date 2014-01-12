from django.db import models
from fluxbb import FLUXBB_PREFIX


class Censoring(models.Model):
    """
    FluxBB Censoring

    Fields on this model match exactly with those defined by fluxbb, see the
    [fluxbb dbstructure](http://fluxbb.org/docs/v1.5/dbstructure#users).
    """
    id = models.AutoField(primary_key=True)
    search_for = models.CharField(max_length=60, default="")
    replace_with = models.CharField(max_length=60, default="")

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'censoring'
