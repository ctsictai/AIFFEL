from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone


class UserManager(BaseUserManager):
    """
    Customized BaseUserManager
    """

    def create_user(self, identification, password, **extra_fields):
        if not identification:
            raise ValueError("The given identification must be set")
        # identification = self.identification
        user = self.model(identification=identification, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, identification, password, **extra_fields):

        return self.create_user(identification, password, **extra_fields)


class User(AbstractBaseUser):
    """
    Customized AbstractBaseUser
    """

    identification = models.CharField(max_length=30, unique=True)
    username = models.CharField(max_length=30, blank=True, null=True)

    is_active = models.BooleanField(("active"), default=True,)
    date_joined = models.DateTimeField(("date joined"), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "identification"

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.identification
