from django.db import models
from fluxbb import FLUXBB_PREFIX
from .fluxbb_fields import UnixTimestampField


class Topics(models.Model):
    """
    FluxBB Topics

    Fields on this model match with those defined by fluxbb, see the
    [fluxbb dbstructure](http://fluxbb.org/docs/v1.5/dbstructure#users).
    However, the following changes have been made.

    topic.last_post references the last 'fluxbb.Posts' object.
    topic.last_post_time gets the time of the last post.
    """
    id = models.AutoField(primary_key=True)
    poster = models.CharField(max_length=200, default="")
    subject = models.CharField(max_length=255, default="")
    posted = models.IntegerField(max_length=10, default=0)
    first_post = models.ForeignKey('fluxbb.Posts', related_name='first_post',
                                   db_constraint=False)
    last_post = models.ForeignKey('fluxbb.Posts', related_name='last_post',
                                  db_constraint=False)
    last_post_time = UnixTimestampField(db_column='last_post')
    last_poster = models.CharField(max_length=200, blank=True, null=True,
                                   default=None)

    # TODO - mediumint field
    num_views = models.IntegerField(max_length=8, default=0)
    num_replies = models.IntegerField(max_length=8, default=0)

    closed = models.BooleanField(default=False)
    sticky = models.BooleanField(default=False)
    moved_to = models.ForeignKey('fluxbb.Topics', db_column='moved_to',
                                 db_constraint=False, blank=True, null=True,
                                 default=None)
    forum = models.ForeignKey('fluxbb.Forums', db_constraint=False)

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'topics'
