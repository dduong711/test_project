from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

from .models import Organization
from .forms import OrganizationCreationForm

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationCreationForm
    template_name = "organization/create.html"
    success_url = reverse_lazy("organization:detail")

    def form_valid(self, form):
        self.object = form.save(username=self.request.user.username)
        return redirect(self.get_success_url())


class OrganizationDetailView(DetailView):
    model = Organization
    template_name = "organization/detail.html"

    def get_object(self, query_set=None):
        return self.request.user.organization

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.user_type == "OR":
            return super().dispatch(request, *args, **kwargs)
        return redirect(reverse("users:detail", kwargs={"username": self.request.user.username}))
