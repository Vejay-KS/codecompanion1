from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CodeCompanionUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email = models.EmailField()
    password1=models.CharField(max_length=200)
    password2=models.CharField(max_length=200)

    class UserRoles(models.TextChoices):
        SOFTWAREDEVELOPER = "SOFTWAREDEVELOPER", 'Software Developer'
        SOFTWAREDEVELOPMENTMANAGER = "SOFTWAREDEVELOPMENTMANAGER", 'Software Development Manager'
        HUMANRESOURCEMANAGER = "HUMANRESOURCEMANAGER", 'Human Resource Manager'

    BASE_ROLE = UserRoles.SOFTWAREDEVELOPER
    ROLE = models.CharField(max_length=50, choices=UserRoles.choices, default=BASE_ROLE)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password1', 'password2', 'email', 'ROLE']

class CodeCompanionSD(CodeCompanionUser):
    LEVEL_CHOICES = ((1, 'Junior'), (2, 'Senior'))
    BASE_ROLE = CodeCompanionUser.BASE_ROLE.SOFTWAREDEVELOPER
    sdlevel = models.CharField(max_length=50, choices=LEVEL_CHOICES)


class CodeCompanionSDM(CodeCompanionUser):
    LEVEL_CHOICES = ((1, 'Junior'), (2, 'Senior'))
    BASE_ROLE = CodeCompanionUser.BASE_ROLE.SOFTWAREDEVELOPMENTMANAGER
    sdmlevel = models.CharField(max_length=50, choices=LEVEL_CHOICES)


class CodeCompanionHRM(CodeCompanionUser):
    LEVEL_CHOICES = ((1, 'Junior'), (2, 'Senior'))
    BASE_ROLE = CodeCompanionUser.BASE_ROLE.HUMANRESOURCEMANAGER
    hrmlevel = models.CharField(max_length=50, choices=LEVEL_CHOICES)
