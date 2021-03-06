from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from .models import Page

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView

from django.urls import reverse, reverse_lazy

from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from . forms import PageForm

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

class StaffRequiredMixin(object):
    """
    This mixing required the user is from the staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        #if not request.user.is_staff: # IS NOT REQUIRED WHEN WE USE THE DECORADOR
        #    return redirect(reverse_lazy('admin:login')) # IS NOT REQUIRED WHEN WE USE THE DECORADOR
        return super(PageCreate, self).dispatch(request, *args, **kwargs)


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

@method_decorator(staff_member_required, name="dispatch")
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    # fields = ['title', 'content', 'order'] # THIS IS IN PAGEFORM SO HERE WE CAN DELETE THIS LINE
    success_url = reverse_lazy('pages:pages')
    # success_url = reversed('pages:page') | THIS IS NOT THE WAY

    # def get_success_url(self) -> str: | THIS IS THE ORIGINAL FUNTION
    #     return super().get_success_url()

    # def get_success_url(self): # THIS IS A WAY TO DO IT | THIS REDIRECT THE PAGE
    #     return reverse('pages:pages')
    # BUT OVERWRITE THE METHOD get IS TEDIOUS IT NOT HAVE SENSE SO USE reverse_laze import it

@method_decorator(staff_member_required, name="dispatch")
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    # fields = ['title', 'content', 'order'] # THIS COMMENT IS BECAUSE FORM CLASS IT HAS IT
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name="dispatch")
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
    