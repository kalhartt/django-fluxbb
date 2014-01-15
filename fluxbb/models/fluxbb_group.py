from django.db import models
from fluxbb import FLUXBB_PREFIX

_null = {'blank': True, 'null': True, 'default': None}


class FluxBBGroup(models.Model):
    """
    FluxBB FluxBBGroup

    Fields on this model match exactly with those defined by fluxbb, see the
    [fluxbb dbstructure](http://fluxbb.org/docs/v1.5/dbstructure#users).
    """
    g_id = models.AutoField(primary_key=True)
    g_title = models.CharField(max_length=50, default="")
    g_user_title = models.CharField(max_length=50, **_null)
    g_moderator = models.BooleanField(default=False)
    g_mod_edit_users = models.BooleanField(default=False)
    g_mod_rename_users = models.BooleanField(default=False)
    g_mod_change_passwords = models.BooleanField(default=False)
    g_mod_ban_users = models.BooleanField(default=False)
    g_read_board = models.BooleanField(default=True)
    g_view_users = models.BooleanField(default=True)
    g_post_replies = models.BooleanField(default=True)
    g_post_topics = models.BooleanField(default=True)
    g_edit_posts = models.BooleanField(default=True)
    g_delete_posts = models.BooleanField(default=True)
    g_delete_topics = models.BooleanField(default=True)
    g_post_links = models.BooleanField(default=True)
    g_set_title = models.BooleanField(default=True)
    g_search = models.BooleanField(default=True)
    g_search_users = models.BooleanField(default=True)
    g_promote_min_posts = models.BooleanField(default=False)
    g_promote_next_group = models.BooleanField(default=False)
    g_send_email = models.BooleanField(default=True)
    g_post_flood = models.SmallIntegerField(max_length=6, default=30)
    g_search_flood = models.SmallIntegerField(max_length=6, default=30)
    g_email_flood = models.SmallIntegerField(max_length=6, default=30)

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'groups'
