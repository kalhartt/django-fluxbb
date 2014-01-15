from django.db import models
from fluxbb import FLUXBB_PREFIX
from .fluxbb_fields import UnixTimestampField

_null = {'blank': True, 'null': True, 'default': None}


class Report(models.Model):
    """
    FluxBB Report

    Fields on this model match exactly with those defined by fluxbb, see the
    [fluxbb dbstructure](http://fluxbb.org/docs/v1.5/dbstructure#users).
    """
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey('fluxbb.Post', db_constraint=False)
    topic = models.ForeignKey('fluxbb.Topic', db_constraint=False)
    forum = models.ForeignKey('fluxbb.Forum', db_constraint=False)
    reported_by = models.ForeignKey(
        'fluxbb.FluxBBUser', db_column='reported_by', db_constraint=False,
        related_name='reported')
    created = UnixTimestampField()
    message = models.TextField(**_null)
    zapped = UnixTimestampField(**_null)
    zapped_by = models.ForeignKey(
        'fluxbb.FluxBBUser', db_column='zapped_by', db_constraint=False,
        related_name='zapped')

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'reports'
