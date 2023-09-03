
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    USER_TYPE = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
    )
    user_type = forms.ChoiceField(choices=USER_TYPE)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'user_type']

        # form.save()
    def save(self, commit=True):
        our_user = super().save(commit=False)  # ami database e data save korbo na ekhn
        if commit == True:
            our_user.save()  # user model e data save korlam
            user_type = self.cleaned_data.get('user_type')
        return our_user
