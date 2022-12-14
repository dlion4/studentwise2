from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings


class CustomeUserManager(BaseUserManager):
    """
    create user by the email
    Args:
        BaseUserManager (email): 
        pass in email as the default authorization
    """

    def create_user(self, email, password, **kwargs):

        if not email:
            raise ValueError(_("Email must be set"))

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError(_("superuser must be set to is_staff=True"))

        if kwargs.get("is_superuser") is not True:
            raise ValueError(_("superuser must be set to is_superuser=True"))

        if kwargs.get("is_active") is not True:
            raise ValueError(_("superuser must be set to is_active=True"))

        return self.create_user(email, password, **kwargs)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomeUserManager()

    def __str__(self):
        return self.email


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profilepic = models.ImageField(
        null=True, blank=True, upload_to="account/{}/".format(user_directory_path))
    first_name = models.CharField(max_length=31, blank=True, null=True)
    last_name = models.CharField(max_length=31, blank=True, null=True)

    def __str__(self):
        return f"{self.user.email}"


def post_save_userprofile_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            UserProfile.objects.create(user=instance, )
        except:
            pass


post_save.connect(post_save_userprofile_model_receiver,
                  sender=settings.AUTH_USER_MODEL)
