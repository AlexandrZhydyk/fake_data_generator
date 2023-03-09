from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

from accounts.forms import LoginForm


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'


class LogoutUser(LoginRequiredMixin, LogoutView):
    pass


class PageNotFoundView(TemplateView):
    template_name = 'accounts/404.html'
    extra_context = {'title': 'Page not found'}


class UnauthorizedView(TemplateView):
    template_name = 'accounts/forbidden.html'
    extra_context = {'title': 'Forbidden'}
