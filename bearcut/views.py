from django.views.generic import TemplateView

class LandingUI(TemplateView):
    template_name = 'bearcut/index.html'
