from django.db import models
from fluxbb import FLUXBB_PREFIX
from .fluxbb_fields import UnixTimestampField

_null = {'blank': True, 'null': True, 'default': None}


class Reports(models.Model):
    """
    FluxBB Reports

    Fields on this model match exactly with those defined by fluxbb, see the
    [fluxbb dbstructure](http://fluxbb.org/docs/v1.5/dbstructure#users).
    """
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey('fluxbb.Posts', db_constraint=False)
    topic = models.ForeignKey('fluxbb.Topics', db_constraint=False)
    forum = models.ForeignKey('fluxbb.Forums', db_constraint=False)
    reported_by = models.ForeignKey('fluxbb.Users', db_column='reported_by',
                                    db_constraint=False,
                                    related_name='reported')
    created = UnixTimestampField()
    message = models.TextField(**_null)
    zapped = UnixTimestampField(**_null)
    zapped_by = models.ForeignKey('fluxbb.Users', db_column='zapped_by',
                                  db_constraint=False, related_name='zapped')

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'reports'
