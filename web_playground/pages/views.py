from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView

from django.urls import reverse, reverse_lazy

from django.views.generic.edit import UpdateView

# Create your views here.
# def pages(request):
#     pages = get_list_or_404(Page)
#     return render(request, 'pages/pages.html', {'pages':pages})

class PageListView(ListView):

    model = Page

# def page(request, page_id, page_slug):
#     page = get_object_or_404(Page, id=page_id)
#     return render(request, 'pages/page.html', {'page':page})

class PageDetailView(DetailView):

    model = Page

class PageCreate(CreateView):
    model = Page
    fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages:pages')
    # success_url = reversed('pages:page') | THIS IS NOT THE WAY

    # def get_success_url(self) -> str: | THIS IS THE ORIGINAL FUNTION
    #     return super().get_success_url()

    # def get_success_url(self): # THIS IS A WAY TO DO IT | THIS REDIRECT THE PAGE
    #     return reverse('pages:pages')
    # BUT OVERWRITE THE METHOD get IS TEDIOUS IT NOT HAVE SENSE SO USE reverse_laze import it

class PageUpdate(UpdateView):
    model = Page
    fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'