from django.db import models
from fluxbb import FLUXBB_PREFIX


class Categories(models.Model):
    """
    FluxBB Categories

    Fields on this model match exactly with those defined by fluxbb, see the
    [fluxbb dbstructure](http://fluxbb.org/docs/v1.5/dbstructure#users).
    """
    id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=80, default="New Category")
    disp_position = models.IntegerField(max_length=10, default=0)

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'categories'
