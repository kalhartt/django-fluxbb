from django.db import models
from fluxbb import FLUXBB_PREFIX
from fluxbb_fields import UnixTimestampField

_null = {'blank': True, 'null': True, 'default': None}


class Forums(models.Model):
    """
    FluxBB Forums

    Fields on this model match with those defined by fluxbb, see the
    [fluxbb dbstructure](http://fluxbb.org/docs/v1.5/dbstructure#users).
    However, the following changes have been made

    forum.last_post references the last 'fluxbb.Posts' object
    forum.last_post_time gives the datetime for the last post
    """
    id = models.AutoField(primary_key=True)
    forum_name = models.CharField(max_length=80, default="New forum")
    forum_desc = models.TextField(**_null)
    redirect_url = models.CharField(max_length=100, **_null)

    # TODO - Make custom field so this handles an iterable of fluxbb.Users
    moderators = models.TextField(**_null)

    # TODO - Set these two fields to use mediumint storage
    num_topics = models.IntegerField(max_length=8, default=0)
    num_posts = models.IntegerField(max_length=8, default=0)

    last_post = models.ForeignKey('fluxbb.Posts', db_index=False,
                                  db_constraint=False, **_null)
    last_post_time = UnixTimestampField(db_column='last_post', **_null)

    last_poster = models.CharField(max_length=200, **_null)
    sort_by = models.BooleanField()
    disp_position = models.IntegerField(max_length=10, default=0)
    cat_id = models.IntegerField(max_length=10, default=0)

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'forums'
