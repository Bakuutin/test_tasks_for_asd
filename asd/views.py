from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse


class LoginView(TemplateView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('account'))
        return super().dispatch(request, *args, **kwargs)
