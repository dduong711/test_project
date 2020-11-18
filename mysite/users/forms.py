from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from django.shortcuts import reverse, redirect

from allauth.account.forms import SignupForm, LoginForm


User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):

    error_message = admin_forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])


class CustomSignupForm(SignupForm):
    ACCOUNT_TYPE = (
        ('IN','Individual'),
        ('OR','Organization')
    )
    user_type = forms.ChoiceField(choices=ACCOUNT_TYPE, widget=forms.RadioSelect)

    def save(self, request):
        user = super().save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user


class CustomLoginForm(LoginForm):
    
    def login(self, request, redirect_url=None):
        ret = super().login(request, redirect_url=None)
        print("???", self.user.user_type)
        if self.user:
            if self.user.user_type == "OR":
                try:
                    _ = self.user.organization
                except Exception:
                    return redirect(reverse("organization:create"))
                else:
                    return redirect(reverse("organization:detail"))
        return ret

