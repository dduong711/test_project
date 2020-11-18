from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ForeignKey, SET_NULL
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for mysite."""
    ACCOUNT_TYPE = (
        ('IN', 'Individual'),
        ('OR', 'Organization')
    )

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    user_type = CharField(max_length=2, choices=ACCOUNT_TYPE, default="IN")

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
