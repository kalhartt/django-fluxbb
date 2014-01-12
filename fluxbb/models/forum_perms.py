"""
FluxBB ForumPermissions Model

This table uses a composite primary key which django currently does not
support, see the [discussion
here](https://code.djangoproject.com/wiki/MultipleColumnPrimaryKeys). As such
it is not included by default. To use the implementation below, you must
manually modify the 'forum_perms' table to the following. Then set
`FLUXBB_COMPOSITEKEYFIX = True` in your settings.py.

```
    id INT NOT NULL,
    ...
    CONSTRAINT `PRIMARY` PRIMARY KEY (id)
```
"""
from django.db import models
from fluxbb import FLUXBB_PREFIX


class ForumPermissions(models.Model):
    """
    FluxBB Forum Permissions

    Fields on this model match exactly with those defined by fluxbb, see the
    [fluxbb dbstructure](http://fluxbb.org/docs/v1.5/dbstructure#users).
    """
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey('fluxbb.Groups', db_constraint=False)
    forum = models.ForeignKey('fluxbb.Forums', db_constraint=False)
    read_forum = models.BooleanField(default=True)
    post_replies = models.BooleanField(default=True)
    post_topics = models.BooleanField(default=True)

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'forum_perms'
        unique_together = ('group', 'forum')
