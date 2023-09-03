from django.db import models
from django.contrib.auth.models import User
# django amaderke built in user niye kaj korar facility dey


class UserDetails(models.Model):
    USER_TYPE = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
    )
    user = models.OneToOneField(
        User, related_name='account', on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
