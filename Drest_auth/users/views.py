from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from .forms import CustomUserCreationForm

class HomePageView(TemplateView):
    template_name = 'home.html'


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'