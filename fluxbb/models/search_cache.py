from django.db import models
from fluxbb import FLUXBB_PREFIX


class SearchCache(models.Model):
    """
    FluxBB Search Cache

    Fields on this model match exactly with those defined by fluxbb, see the
    [fluxbb dbstructure](http://fluxbb.org/docs/v1.5/dbstructure#users).
    """
    id = models.AutoField(primary_key=True)
    ident = models.CharField(max_length=200, default="")
    search_data = models.TextField(blank=True, null=True, default=None)

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'search_cache'
