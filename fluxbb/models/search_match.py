"""
FluxBB SearchMatches Model

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


class SearchMatch(models.Model):
    """
    FluxBB Search Match

    Fields on this model match exactly with those defined by fluxbb, see the
    [fluxbb dbstructure](http://fluxbb.org/docs/v1.5/dbstructure#users).
    """
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey('fluxbb.Post', db_constraint=False)
    word = models.ForeignKey('fluxbb.SearchWord', db_constraint=False)
    subject_match = models.BooleanField(default=False)

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'search_matches'
        unique_together = ('post', 'word')
