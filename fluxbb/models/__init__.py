from .bans import Bans
from .categories import Categories
from .censoring import Censoring
from .config import Config
from .forums import Forums
from .groups import Groups
from .online import Online
from .posts import Posts
from .reports import Reports
from .search_cache import SearchCache
from .search_words import SearchWords
from .topics import Topics
from .users import Users, FluxBBUserManager
from fluxbb import FLUXBB_COMPOSITEKEYFIX

__all__ = ['Bans', 'Categories', 'Censoring', 'Config', 'Forums', 'Groups',
           'Online', 'Posts', 'Reports', 'SearchCache', 'SearchWords',
           'Topics', 'Users', 'FluxBBUserManager']

if FLUXBB_COMPOSITEKEYFIX:
    from .forum_perms import ForumPermissions
    from .forum_subscriptions import ForumSubscriptions
    from .search_matches import SearchMatches
    from .topic_subscriptions import TopicSubscriptions
    __all__ += ('ForumPermissions', 'ForumSubscriptions', 'SearchMatches',
                'TopicSubscriptions')
