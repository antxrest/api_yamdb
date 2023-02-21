from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'

    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (MODERATOR, 'moderator'),
        (USER, 'user'))

<<<<<<< HEAD
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(verbose_name='email',unique=True, max_length=254)
    role = models.CharField('Роли пользователей', default=USER, choices=ROLE_CHOICES, max_length=40)
=======
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(verbose_name='email', unique=True)
    role = models.CharField('Роли пользователей', default=USER, choices=ROLE_CHOICES, max_length=50)
>>>>>>> a2f03a73d36e01291e8e6dc2266d883199ed5fad
    bio = models.TextField('Биография', blank=True, )
    confirmation_code = models.CharField(
        max_length=150,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ('username',)

    def __str__(self):
        return "{}".format(self.username)

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_user(self):
        return self.role == self.USER
