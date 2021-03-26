from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class User(AbstractUser):
    """ Custom User Model"""

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO = "kakao"
    LOGIN_CHOICES = ((LOGIN_EMAIL, "Email"),(LOGIN_GITHUB, "Github"), (LOGIN_KAKAO, "Kakao"))

    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    objects = UserManager() # eb deploy를 할때 command로 createsuperuser를 하기 위해 작성 -> users/management/commands/createsu.py를 보자
