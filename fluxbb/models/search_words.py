from django.db import models
from fluxbb import FLUXBB_PREFIX


class SearchWords(models.Model):
    """
    FluxBB Search Words

    Fields on this model match exactly with those defined by fluxbb, see the
    [fluxbb dbstructure](http://fluxbb.org/docs/v1.5/dbstructure#users).
    """
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=20, default="")

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'search_words'
