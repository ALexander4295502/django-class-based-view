from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)

from . import models


class TeamListView(CreateView, ListView):
    model = models.Team
    fields = ("name", "practice_location", "coach")
    context_object_name = 'teams'
    template_name = "teams/team_list.html"


class TeamDetailView(DetailView, UpdateView):
    fields = ("name", "practice_location", "coach")
    model = models.Team
    template_name = "teams/team_detail.html"


class TeamCreateView(CreateView):
    fields = ("name", "practice_location", "coach")
    model = models.Team

    def get_initial(self):
        initial = super().get_initial()
        initial["coach"] = self.request.user.pk
        return initial


class TeamUpdateView(UpdateView):
    fields = ("name", "practice_location", "coach")
    model = models.Team


class TeamDeleteView(DeleteView):
    model = models.Team
    success_url = reverse_lazy('teams:list')

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return self.model.objects.filter(coach=self.request.user)
        return self.model.objects.all()
