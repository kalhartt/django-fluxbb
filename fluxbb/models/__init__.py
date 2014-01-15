"""
:mod:`fluxbb.models` --- Models wrapping the FluxBB database
------------------------------------------------------------

This module provides access to all of the FluxBB tables as Django models.

.. note::
    Some of FluxBB's tables use composite primary keys, which Django does not
    support. The models for these tables have an auto-incrementing primary key
    field added. To include these models, you must manually modify your
    database to add this column. Then let fluxbb know by setting
    ``FLUXBB_COMPOSITEKEYFIX = True`` in your settings.py.
"""
from fluxbb import FLUXBB_COMPOSITEKEYFIX
from .ban import Ban
from .category import Category
from .censor import Censor
from .config import Config
from .forum import Forum
from .fluxbb_group import FluxBBGroup
from .fluxbb_user import FluxBBUser as FluxBBUser
from .fluxbb_user import FluxBBUserManager
from .online import Online
from .post import Post
from .report import Report
from .search_cache import SearchCache
from .search_word import SearchWord
from .topic import Topic
__all__ = ['Ban', 'Category', 'Censor', 'Config', 'Forum', 'FluxBBGroup',
           'Online', 'Post', 'Report', 'SearchCache', 'SearchWord',
           'Topic', 'FluxBBUser', 'FluxBBUserManager']

if FLUXBB_COMPOSITEKEYFIX:
    from .forum_permission import ForumPermission
    from .forum_subscription import ForumSubscription
    from .search_match import SearchMatch
    from .topic_subscription import TopicSubscription
    __all__ += ('ForumPermission', 'ForumSubscription', 'SearchMatch',
                'TopicSubscription')
