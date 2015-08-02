from django.contrib import messages
from django.core.urlresolvers import reverse
from registration.backends.simple.views import RegistrationView


class CustomRegistrationView(RegistrationView):
    def get_success_url(self, request=None, user=None):
        return reverse('dashboard')

    def form_valid(self, request, form):
        messages.success(request, 'Registration successful. You were logged in!')
        return super(CustomRegistrationView, self).form_valid(request, form)

custom_registration_view = CustomRegistrationView.as_view()
