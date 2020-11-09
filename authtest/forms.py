from django.contrib.auth.forms import UserCreationForm

from authtest.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'password1', 'password2', 'role']
