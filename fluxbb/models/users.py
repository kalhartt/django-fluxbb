from django.contrib import auth
from django.contrib.auth.models import BaseUserManager, Group, Permission
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from fluxbb import FLUXBB_PREFIX
from fluxbb_fields import UnixTimestampField
import hashlib

_null = {'blank': True, 'null': True, 'default': None}


class FluxBBUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=FluxBBUserManager.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given username, email, and
        password.
        """
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            group_id=1,
            username=username,
            email=FluxBBUserManager.normalize_email(email),
            registered=timezone.now(),
            last_visit=timezone.now()
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class Users(models.Model):
    """
    FluxBB User Model

    This user model should have all the extras needed to use as a custom user
    model by adding `AUTH_USER_MODEL = 'fluxbb.Users'`. It supports the
    `AbstractBaseUser` and `PermissionsMixin` protocols defined by Django.

    Since FluxBB uses 1-to-1 user/group relations for determining
    active/user/superuser status, the normal django user methods can have
    unexpected consequences. See their documentation on this model for details.

    Fields on this model match exactly with those defined by fluxbb, see the
    [fluxbb dbstructure](http://fluxbb.org/docs/v1.5/dbstructure#users).
    All fields defined as `tinyint(1)` are considered BooleanFields and any
    `int(10)` field representing a timestamp is a datetime field implemented
    by a UnixTimestampField.
    """
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey('fluxbb.Groups', db_constraint=False, default=0)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=40)
    email = models.EmailField(max_length=80)
    title = models.CharField(max_length=50, **_null)
    realname = models.CharField(max_length=40, **_null)
    url = models.CharField(max_length=100, **_null)
    jabber = models.CharField(max_length=80, **_null)
    icq = models.CharField(max_length=12, **_null)
    msn = models.CharField(max_length=80, **_null)
    aim = models.CharField(max_length=30, **_null)
    yahoo = models.CharField(max_length=30, **_null)
    location = models.CharField(max_length=30, **_null)
    signature = models.TextField(**_null)
    disp_topics = models.SmallIntegerField(max_length=3, **_null)
    disp_posts = models.SmallIntegerField(max_length=3, **_null)
    email_setting = models.BooleanField(default=True)
    notify_with_post = models.BooleanField(default=False)
    auto_notify = models.BooleanField(default=False)
    show_smilies = models.BooleanField(default=True)
    show_img = models.BooleanField(default=True)
    show_img_sig = models.BooleanField(default=True)
    show_avatars = models.BooleanField(default=True)
    show_sig = models.BooleanField(default=True)
    timezone = models.FloatField(default=0)
    dst = models.BooleanField(default=False)
    time_format = models.BooleanField(default=False)
    date_format = models.BooleanField(default=False)
    language = models.CharField(max_length=25, default="English")
    style = models.CharField(max_length=25, default="Air")
    num_posts = models.IntegerField(max_length=10, default=0)
    last_post = UnixTimestampField(max_length=10, **_null)
    last_search = UnixTimestampField(max_length=10, **_null)
    last_email_sent = UnixTimestampField(max_length=10, **_null)
    registered = UnixTimestampField(max_length=10, auto_now_add=True)
    registration_ip = models.CharField(max_length=39, default="0.0.0.0")
    last_visit = UnixTimestampField(max_length=10, auto_now_add=True)
    admin_note = models.CharField(max_length=30, **_null)
    activate_string = models.CharField(max_length=80, **_null)
    activate_key = models.CharField(max_length=8, **_null)

    # Not part of the FluxBB definition
    groups = models.ManyToManyField(Group, blank=True, related_name="user_set",
                                    related_query_name="user")
    user_permissions = models.ManyToManyField(Permission, blank=True,
                                              related_name="user_set",
                                              related_query_name="user")

    objects = FluxBBUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_username(self):
        """Return the identifying username for this User."""
        return self.username

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username

    def natural_key(self):
        return (self.get_username(),)

    def is_anonymous(self):
        """
        Returns true for Guest users.
        """
        return self.id == 1

    def is_authenticated(self):
        """
        Return False for Guest users
        """
        return self.id != 1

    @property
    def is_active(self):
        """
        FluxBB users are active if they are assigned a group.

        Readonly property, deactivate a member by moving them group g_id=0
        """
        return self.group_id != 0

    @property
    def is_staff(self):
        """
        FluxBB users are staff if they are in the Administrators or Moderators
        group (g_id=1 or g_id=2).

        Readonly property, revoke status by changing their group.
        """
        return self.group_id in (1, 2)

    @property
    def is_superuser(self):
        """
        FluxBB users are superusers if they are an administrator (g_id=1).

        Readonly property, revoke superuser status by changing their group.
        """
        return self.group_id == 1

    def get_full_name(self):
        """Fullname aliases to FluxBB realname."""
        return self.realname

    def get_short_name(self):
        """Shortname aliases to FluxBB username."""
        return self.username

    @property
    def last_login(self):
        """Alias django's last_login to fluxbb's last_visit."""
        return self.last_visit

    @last_login.setter
    def last_login(self, value):
        self.last_visit = value

    @property
    def date_joined(self):
        """Alias django's date_joined to fluxbb's registered."""
        return self.registered

    @date_joined.setter
    def date_joined(self, value):
        self.registered = value

    def set_password(self, raw_password):
        """
        Sets the users password to raw_password. Does not save the user model.
        """
        if not raw_password:
            self.password = ''
        else:
            self.password = hashlib.sha1(raw_password).hexdigest()

    def check_password(self, raw_password):
        """
        Returns True if raw_password is the users password.
        """
        if not self.password:
            return False
        return self.password == hashlib.sha1(raw_password).hexdigest()

    def set_unusable_password(self):
        self.password = ''

    def has_usable_password(self):
        return bool(self.password)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_group_permissions(self, obj=None):
        permissions = set()
        for backend in auth.get_backends():
            if hasattr(backend, "get_group_permissions"):
                permissions.update(backend.get_group_permissions(self, obj))
        return permissions

    def get_all_permissions(self, obj=None):
        permissions = set()
        for backend in auth.get_backends():
            if hasattr(backend, "get_all_permissions"):
                permissions.update(backend.get_all_permissions(self, obj))
        return permissions

    def has_perm(self, perm, obj=None):
        if self.is_superuser:
            return True

        for backend in auth.get_backends():
            if hasattr(backend, "has_perm"):
                if backend.has_perm(self, perm, obj):
                    return True
        return False

    def has_perms(self, perm_list, obj=None):
        return all(self.has_perm(perm, obj) for perm in perm_list)

    def has_module_perms(self, app_label):
        if self.is_superuser:
            return True

        for backend in auth.get_backends():
            if hasattr(backend, "has_module_perms"):
                if backend.has_perm(self, app_label):
                    return True
        return False
