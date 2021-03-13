from django.shortcuts import render

from django.views.generic.base import TemplateView

class HomePageView(TemplateView):

    template_name = "core/home.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = "My Super Web Playground"
    #     return context

    # def get(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
    #     return super().get(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {'title':"My Supper Web PlayGround"})

class SamplePageView(TemplateView):

    template_name = "core/sample.html"
