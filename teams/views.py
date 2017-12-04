from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)

from . import models
from . import mixins


class TeamListView(CreateView, ListView):
    model = models.Team
    fields = ("name", "practice_location", "coach")
    context_object_name = 'teams'
    template_name = "teams/team_list.html"


class TeamDetailView(DetailView, UpdateView):
    fields = ("name", "practice_location", "coach")
    model = models.Team
    template_name = "teams/team_detail.html"


class TeamCreateView(LoginRequiredMixin, mixins.PageTitleMixin, CreateView):
    fields = ("name", "practice_location", "coach")
    page_title = "Create a new team"
    model = models.Team

    def get_initial(self):
        initial = super().get_initial()
        initial["coach"] = self.request.user.pk
        return initial


class TeamUpdateView(LoginRequiredMixin, mixins.PageTitleMixin, UpdateView):
    fields = ("name", "practice_location", "coach")
    model = models.Team

    def get_page_title(self):
        object = self.get_object()
        return "Update {}".format(object.name)


class TeamDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Team
    success_url = reverse_lazy('teams:list')

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return self.model.objects.filter(coach=self.request.user)
        return self.model.objects.all()
