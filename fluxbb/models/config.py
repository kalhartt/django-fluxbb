from django.db import models
from fluxbb import FLUXBB_PREFIX


class Config(models.Model):
    """
    FluxBB Config

    Model Fields:
        conf_name (str): Name of the configuration variable. General
            configuration options start with the prefix o_ and general
            permission options start with the prefix p_
        conf_value (str): Value of the configuration variable
    """
    conf_name = models.CharField(max_length=255, default="", primary_key=True)
    conf_value = models.TextField(blank=True, null=True, default=None)

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'config'
