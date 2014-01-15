from django.db import models
from fluxbb import FLUXBB_PREFIX


class Censor(models.Model):
    """
    FluxBB Censor

    Model Fields:
        id (int): Auto incrementing primary key for the model
        search_for (str): The term to search for
        replace_with (str): The term to replace with
    """
    id = models.AutoField(primary_key=True)
    search_for = models.CharField(max_length=60, default="")
    replace_with = models.CharField(max_length=60, default="")

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'censoring'
