from django import forms
from django.contrib.auth import get_user_model

from .models import Organization

User = get_user_model()

class OrganizationCreationForm(forms.ModelForm):

    class Meta:
        model = Organization
        fields = ("name", )

    def save(self, username, commit=True):
        organization = super().save(commit=False)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Exception("User Not Found")
        organization.owner = user
        organization.save()
        return organization
 