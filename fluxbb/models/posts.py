from django.db import models
from fluxbb import FLUXBB_PREFIX
from fluxbb_fields import UnixTimestampField

_null = {'blank': True, 'null': True, 'default': None}


class Posts(models.Model):
    """
    FluxBB Posts

    Fields on this model match with those defined by fluxbb, see the
    [fluxbb dbstructure](http://fluxbb.org/docs/v1.5/dbstructure#users).
    However, the following changes have been made

    post.poster references the 'fluxbb.Users' object for the poster
    post.poster_name references the poster's username
    """
    id = models.AutoField(primary_key=True)
    poster = models.ForeignKey('fluxbb.Users', db_constraint=False)
    poster_name = models.CharField(max_length=200, default="",
                                   db_column='poster')
    poster_ip = models.CharField(max_length=39, **_null)
    poster_email = models.CharField(max_length=80, **_null)
    message = models.TextField(**_null)
    hide_smilies = models.BooleanField(default=False)
    posted = UnixTimestampField(auto_now_add=True)
    edited = UnixTimestampField(**_null)
    edited_by = models.CharField(max_length=200, **_null)
    topic = models.ForeignKey('fluxbb.Topics', db_constraint=False)

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'posts'
