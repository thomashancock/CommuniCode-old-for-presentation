from django.http import Http404
from django.views.generic import TemplateView
from communicode.gitlab_api import wrappers

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context_data = super(DashboardView, self).get_context_data(**kwargs)
        context_data['projects'] = wrappers.get_projects()
        return context_data

dashboard_view = DashboardView.as_view()


class ProjectCodeView(TemplateView):
    template_name = 'projectcode.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectCodeView, self).get_context_data(**kwargs)
        project_id = kwargs.get('project_id')
        project = wrappers.get_project(int(project_id))
        if not project:
            raise Http404
        context['project'] = project
        context['last_commit'] = wrappers.get_commit(project_id, 'master')
        return context

project_code_view = ProjectCodeView.as_view()
