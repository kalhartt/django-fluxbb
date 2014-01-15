from django.db import models
from fluxbb import FLUXBB_PREFIX
from .fluxbb_fields import UnixTimestampField

_null = {'blank': True, 'null': True, 'default': None}


class Forum(models.Model):
    """
    FluxBB Forum

    Model Fields:
        id (int): Auto incrementing primary key for the model
        forum_name (str): Name of the forum
        forum_desc (str): Description of the forum (may contain HTML)
        redirect_url (str): URL to redirect users to upon clicking the forum
            link, or None for a normal forum
        moderators (str): A serialized associative PHP array with moderator
            names -> user IDs
        num_topics (int): Number of topics the forum contains
        num_posts (int): Number of posts the forum contains
        last_post (Post): Last Post object made in the forum.
        last_post_time (datetime): Time the last post was made in the forum
        last_poster (str): Username (or guest name) of the user that made the
            last post in the forum
        sort_by (bool): How the posts in the forum should be sorted. ``False``
            sorts by last post time, ``True`` by topic start time
        disp_position (int): The position of this forum in relation to others.
        category (Category): The Category in which this forum resides
    """
    # TODO - Make custom field so `moderators` handles an iterable of
    # fluxbb.FluxBBUsers
    # TODO - Set `num_topics` and `num_posts` fields to use mediumint storage
    id = models.AutoField(primary_key=True)
    forum_name = models.CharField(max_length=80, default="New forum")
    forum_desc = models.TextField(**_null)
    redirect_url = models.CharField(max_length=100, **_null)
    moderators = models.TextField(**_null)
    num_topics = models.IntegerField(max_length=8, default=0)
    num_posts = models.IntegerField(max_length=8, default=0)
    last_post = models.ForeignKey('fluxbb.Post', db_index=False,
                                  db_constraint=False, **_null)
    last_post_time = UnixTimestampField(db_column='last_post', **_null)
    last_poster = models.CharField(max_length=200, **_null)
    sort_by = models.BooleanField()
    disp_position = models.IntegerField(max_length=10, default=0)
    category = models.ForeignKey('fluxbb.Category', db_index=False,
                                 db_column='cat_id')

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'forums'
