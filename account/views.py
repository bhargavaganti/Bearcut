from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from django.views import generic
from . import forms

class SignupUI(CreateView):
    form_class = forms.SignupForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'

class LoginUI(generic.FormView):
    form_class = forms.LoginForm
    success_url = reverse_lazy('landing')
    template_name = 'account/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginUI, self).form_valid(form)
        else:
            return self.form_invalid(form)
