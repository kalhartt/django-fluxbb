"""
FluxBB ForumSubscriptions Model

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


class ForumSubscription(models.Model):
    """FluxBB Forum Subscription"""
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('fluxbb.FluxBBUser', db_constraint=False)
    forum = models.ForeignKey('fluxbb.Forum', db_constraint=False)

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'forum_subscriptions'
        unique_together = ('user', 'forum')
