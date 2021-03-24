# Web Playground Project

In this repositoy I will be getting the documentation of the proyect web playgorund, class base view

# Index

1. [How to upload this repository](#How-to-upload-this-repository)
2. [Create Virtual Environment With Conda](#Create-Virtual-Environment-With-Conda)
3. [Password Login](#Password-Login)
4. [Requirements](#Requirements)
5. [Documentation](#Documentation-Web-Playground)
   1. [First CBV and Template View](#First-CBV-and-Template-View)
   2. [Config App Pages](#Config-App-Pages)
   3. [ListView and DetailView](#ListView-and-DetailView)
   4. [CRUD Views CBV Create View](#CRUD-Views-CBV-Create-View)
   5. [CRUD Views CBV UpdateView](#CRUD-Views-CBV-UpdateView)
   6. [CRUD Views CBV DeleteView](#CRUD-Views-CBV-DeleteView)
   7. [Forms for Models in CBV](#Forms-for-Models-in-CBV)
   8. [Create a Id Mixing](#Create-a-Id-Mixing)
   9. [Using ID Decorators](#Using-ID-Decorators)
   10. [8th App "Registration" Start Session](#8th-App-"Registration"-Start-Session)
   11. [Closing the session](#Closing-the-session)
   12. [Register with CBV](#Register-with-CBV)
   13. [Beauty Register with CBV](#Beauty-Register-with-CBV)
   14. [Obligatory EMAIL](#Obligatory-EMAIL)
   15. [Unique Email](#Unique-Email)
   16. [Password Forget?](#Password-Forget?)
   17. [User Profile](#User-Profile)
   18. [Editable Profile](#Editable-Profile)
   19. [Beauty Profile Form](#Beauty-Profile-Form)
   20. [Edit Email](#Edit-Email)
   21. [Intro To Signals](#Intro-To-Signals)
   22. [Intro to Unit Test](#Intro-to-Unit-Test)
   23. [Optimizing Avatar Storage](#Optimizing-Avatar-Storage)
   24. [9th App Public Profiles](#9th-App-Public-Profiles)
   25. [Pagination Of Results List View](#Pagination-Of-Results-List-View)
   26. [10 App Messenger](10-App-Messenger)
   27. [TDD 1 Firts Test](#TDD-1-Firts-Test)
6. [Comments](#Comments)

# How to upload this repository

[Index](#Index)

- Creo el repo en github normal si novedad, en blanco.
- Creo el README.md con la estructura de documentacion como puedes ver.
- **Y luego aplico estos comandos:**

  - git init
  - git add .
  - git commit -m "first commit"
  - git branch -M main
  - git remote add origin https://github.com/gustavcaves/web_playground_project.git
  - git push -u origin main
- **Luego para seguir actualizando:**

  - git status
  - **git add .**
  - git status
  - **git commit -m "another commit"**
  - git status
  - **git push -u origin main**

# Create Virtual Environment With Conda

[Index](#Index)

- conda create -n py392_webplayground python=3.9.2
- activate : $ conda activate py392_webplayground
- deactivate : $ conda deactivate

# Password Login

[Index](#Index)

admin | 1234

# Link de Post

[Index](#Index)

# Requirements

[Index](#Index)

pip freeze > requirements.txt

# Documentation Web Playground

[Index](#Index)

## First CBV and Template View

[Index](#Index)

To create our first CBV “Class Base View” we use the Template View. We have a page [http://ccbv.co.uk/](http://ccbv.co.uk/) where we find the Template View, and the step are next:

In views.py

```
from django.shortcuts import render
 
from django.views.generic.base import TemplateView
 
class HomePageView(TemplateView):
 
    template_name = "core/home.html"
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "My Super Web Playground"
        return context
 
class SamplePageView(TemplateView):
 
    template_name = "core/sample.html"
```

And in urls.py

```
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('sample/', views.SamplePageView.as_view(), name="sample"),
]
```

Then we overwrite the metod get():

```
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
```

Here is the github repository:

[https://github.com/gustavcaves/web_playground_project](https://github.com/gustavcaves/web_playground_project)

## Config App Pages

[Index](#Index)

settings.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'pages.apps.PagesConfig',
    'ckeditor',
]
```

CMD

```
python manage.py makemigrations pages
 
python manage.py migrate pages
 
python manage.py createsuperuser
```

core/urls.py

```
urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
]
```

core/templates/core/base.html

```
<li class="nav-item">
  <a class="nav-link" href="{% url 'pages' %}">Páginas</a>
</li
```

pages/views.py

```
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page
 
# Create your views here.
def pages(request):
    pages = get_list_or_404(Page)
    return render(request, 'pages/pages.html', {'pages':pages})
 
def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/page.html', {'page':page})
```

We create a some examples for pages. Before that we need ckeditor working on.

In this links copy some text [https://www.lipsum.com/](https://www.lipsum.com/) .

## ListView and DetailView

[Index](#Index)

[http://ccbv.co.uk/projects/Django/3.1/django.views.generic.list/ListView/](http://ccbv.co.uk/projects/Django/3.1/django.views.generic.list/ListView/)

[https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-display/#django.views.generic.list.ListView](https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-display/#django.views.generic.list.ListView)

pages/views.py

```
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page
 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
 
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
```

pages/urls.py

```
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', views.PageDetailView.as_view(), name='page'),
]
```

pages/templates/page change the name of the html pages and page for

page_detail.html

page_list.html

And in the for in page_list.html

`{% for page in page_list %}`

The objects is call through page_list

## CRUD Views CBV Create View

[Index](#Index)

Create a new file named pages_menu.html in pages/templates/includes with the next code:

```
{% if request.user.is_staff %}
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container">
    <span class="navbar-brand" href="#"><i>Administrar</i></span>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#nep" aria-controls="nep" aria-expanded="false">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="nep">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <a class="nav-link" href="#"><i>Crear página</i></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'pages' %}"><i>Listar páginas</i></a>
        </li>
      </ul>
    </div>
  </div>
</nav>
{% endif %}
```

Add this in each page html, page_list and page_detail:

`{% include 'pages/includes/pages_menu.html' %}`

CreateView

[http://ccbv.co.uk/projects/Django/3.1/django.views.generic.edit/CreateView/](http://ccbv.co.uk/projects/Django/3.1/django.views.generic.edit/CreateView/)

[https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView](https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView)

pages/views.py

```
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page
 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
 
from django.views.generic.edit import CreateView
 
from django.urls import reverse, reverse_lazy
 
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
```

In pages/urls.py

```
from django.urls import path
from . import views
 
pages_patterns = ([
    path('', views.PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', views.PageDetailView.as_view(), name='page'),
    path('create/', views.PageCreate.as_view(), name='create'),
], 'pages')
```

In web_playground/urls.py

```
from django.contrib import admin
from django.urls import path, include
from pages.urls import pages_patterns
 
urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include(pages_patterns)),
    path('admin/', admin.site.urls),
]
```

In core/base.html

```
<li class="nav-item">
  <a class="nav-link" href="{% url 'pages:pages' %}">Páginas</a>
</li>
```

In pages/templates/pages/includes/pages_menu.html

```
<li class="nav-item">
  <a class="nav-link" href="{% url 'pages:create' %}"><i>Crear página</i></a>
</li>
<li class="nav-item">
  <a class="nav-link" href="{% url 'pages:pages' %}"><i>Listar páginas</i></a>
</li>
```

In page/templates/page/page_list.html

`{% for page in page_list|dictsort:"id" reversed %}`

Then we create a form in pages/templates/pages/ call it page_form with the next code:

```
{% extends 'core/base.html' %}
{% load static %}
{% block title %}Crear página{% endblock %}
{% block content %}
{% include 'pages/includes/pages_menu.html'%}
<main role="main">
  <div class="container">
    <div class="row mt-3">
      <div class="col-md-9 mx-auto">
        <div>
            <form action="" method="post">{% csrf_token %}
                <table>
                    {{ form.as_table }}
                </table>
                <br>
                <input type="submit" value="Crear página" />
            </form>
        </div>
      </div>
    </div>
  </div>
</main>
{% endblock %}
```

## CRUD Views CBV UpdateView

[Index](#Index)

In page/views.py

```
class PageUpdate(UpdateView):
    model = Page
    fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'
 
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

```

In page/urls.py

```
from django.urls import path
from . import views
 
pages_patterns = ([
    path('', views.PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', views.PageDetailView.as_view(), name='page'),
    path('create/', views.PageCreate.as_view(), name='create'),
    path('update/<int:pk>', views.PageUpdate.as_view(), name='update'),
], 'pages')
```

Create a new file template name page_update_form.html

```
{% extends 'core/base.html' %}
{% load static %}
{% block title %}Actualizar página{% endblock %}
{% block content %}
{% include 'pages/includes/pages_menu.html'%}
<main role="main">
  <div class="container">
    <div class="row mt-3">
      <div class="col-md-9 mx-auto">
        <div>
        {% if 'ok' in request.GET %}
          <p class="alert alert-success">Página editada correctamente.
          <a href="{% url 'pages:page' page.id page.title|slugify %}">Haz clic aqui para ver el resultado.</a>
          </p>
        {% endif %}
            <form action="" method="post">{% csrf_token %}
                <table>
                    {{ form.as_table }}
                </table>
                <br>
                <input type="submit" value="Actualizar página" />
            </form>
        </div>
      </div>
    </div>
  </div>
</main>
{% endblock %}
```

In page_detail.html

`p a href="{% url 'pages:update' page.id %}">Editar /a/p`

In page_list.html

```
{% if request.user.is_staff %}
  | <a href="{% url 'pages:update' page.id %}">Editar</a>
<!--
  | <a href="#">Borrar</a>
-->
{% endif %}
Thats all friends
```

## CRUD Views CBV DeleteView

[Index](#Index)

In pages/views.py

```
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
```

In pages/urls.py

```
path('delete/<int:pk>', views.PageDelete.as_view(), name='delete'),

```

In pages/templates/pages create a new file called page_confirm_delete.html with the next code:

```
{% extends 'core/base.html' %}
{% load static %}
{% block title %}Borrar página{% endblock %}
{% block content %}
{% include 'pages/includes/pages_menu.html'%}
<main role="main">
  <div class="container">
    <div class="row mt-3">
      <div class="col-md-9 mx-auto">
        <div>
            <form action="" method="post">{% csrf_token %}
                <p>¿Estás seguro de que quieres borrar "{{ object }}"?</p>
                <input type="submit" value="Sí, borrar la página" />
            </form>
        </div>
      </div>
    </div>
  </div>
</main>
{% endblock %}
```

## Forms for Models in CBV

[Index](#Index)

In pages/views.py

```
from . forms import PageForm
 
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    # fields = ['title', 'content', 'order'] # THIS IS IN PAGEFORM SO HERE WE CAN DELETE THIS LINE
    success_url = reverse_lazy('pages:pages')
    # success_url = reversed('pages:page') | THIS IS NOT THE WAY 
 
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    # fields = ['title', 'content', 'order'] # THIS COMMENT IS BECAUSE FORM CLASS IT HAS IT
    template_name_suffix = '_update_form'
```

Create a file named forms.py in pages

```
from django import forms # THIS IS FOR HAVE THE STRUCTURE OF THE FORMS
from .models import Page # THIS LINKS THE MODELS PAGE FOR GENERATE AUTOMATIC
 
class PageForm(forms.ModelForm): # WE CREATE THE FORM MODEL
 
    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Orden'}),
        }
        labels = {
            'title':'','order':'','content':''
        }
```

In pages/admin.py

```
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
 
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

```

In pages/page_update_form.py

```
    <form action="" method="post">{% csrf_token %}
            {{ form.as_p }}
        <div class="text-center">
        <input type="submit" class="btn btn-primary btn-block" value="Actualizar página" />
        </div>
    </form>
</div>
```

In page/page_form.html

```
<form action="" method="post">{% csrf_token %}
        {{ form.as_p }}
    <div class="text-center">
    <input type="submit" class="btn btn-primary btn-block" value="Crear página" />
    </div>
</form>
```

In page/page_confirm_delete.html

```
<form action="" method="post">{% csrf_token %}
    <p>¿Estás seguro de que quieres borrar <b>"{{ object }}"</b>?</p>
    <input type="submit" class="btn btn-primary btn-block" value="Sí, borrar la página" />
</form>
```

In pages/include/pages_menu.html

```
<link href="{% static 'pages/css/custom_ckeditor.css' %}" rel="stylesheet">

```

[https://github.com/django-ckeditor/django-ckeditor](https://github.com/django-ckeditor/django-ckeditor)

[https://github.com/django-ckeditor/django-ckeditor#outside-of-django-admin](https://github.com/django-ckeditor/django-ckeditor#outside-of-django-admin)

CSS de Ckeditor

### static/pages/css/custom_ckeditor.css

```css
.django-ckeditor-widget, .cke_editor_id_content {
    width: 100% !important;
    max-width: 821px !important;
}
```

### Inyectar en pages_menu.html

```html
<link href="{% static 'pages/css/custom_ckeditor.css' %}" rel="stylesheet">
```

### Inyectar en admin.py

```python
from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
  
    # Inyectamos nuestro fichero css
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }
  
admin.site.register(Page, PageAdmin)
```

## Create a Id Mixing

[Index](#Index)

As our views that we have created are publick we need to solve this problem.

```
class StaffRequiredMixin(object):
    """
    This mixing required the user is from the staff
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(PageCreate, self).dispatch(request, *args, **kwargs)


```

And for each class view we add the StaffRequiredMixin as priority

`class PageCreate(StaffRequiredMixin, CreateView):`

`class PageUpdate(StaffRequiredMixin, UpdateView):`

`class PageDelete(StaffRequiredMixin, DeleteView):`

## Using ID Decorators

[Index](#Index)

pages/views.py

```
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
```

```
class StaffRequiredMixin(object):
    """
    This mixing required the user is from the staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        #if not request.user.is_staff: # IS NOT REQUIRED WHEN WE USE THE DECORADOR
        #    return redirect(reverse_lazy('admin:login')) # IS NOT REQUIRED WHEN WE USE THE DECORADOR
        return super(PageCreate, self).dispatch(request, *args, **kwargs)
```

for each class view

```
@method_decorator(staff_member_required, name="dispatch")
class PageCreate(CreateView):
```

```
@method_decorator(staff_member_required, name="dispatch")
class PageUpdate(UpdateView):
```

```
@method_decorator(staff_member_required, name="dispatch")
class PageDelete(DeleteView):
```

Now in the url it show us a new data that is ?next= who redirect us a the indicated page

http://127.0.0.1:8000/admin/login/?next=/pages/create/

## 8th App "Registration" Start Session

[Index](#Index)

The name will be "registration"

`(py392_webplayground) C:\www_dj\web_playground\web_playground>python manage.py startapp registration`

urls.py general

```
    # Path Auth
    path('accounts/', include('django.contrib.auth.urls')),
```

Then go to:

http://127.0.0.1:8000/accounts

And you will see

Using the URLconf defined in `web_playground.urls`, Django tried these URL patterns, in this order:

1. [name='home']
2. sample/ [name='sample']
3. pages/
4. admin/
5. accounts login/ [name='login']
6. accounts logout/ [name='logout']
7. accounts password_change/ [name='password_change']
8. accounts password_change/done/ [name='password_change_done']
9. accounts password_reset/ [name='password_reset']
10. accounts password_reset/done/ [name='password_reset_done']
11. accounts reset/<uidb64>/<token>/ [name='password_reset_confirm']
12. accounts reset/done/ [name='password_reset_complete']

The current path, `accounts`, didn't match any of these.

http://ccbv.co.uk/ | AUTH VIEWS

Only we have to establish the templates or extend if we need do it

If we go to accounts/login it show us a typical error template, so we need to create it

So create a file in registrations/templates/registration called login.html with the nex code:

https://gist.github.com/gustavcaves/38b56718be23000c61be51767e54b90a

```
{% extends 'core/base.html' %}
{% load static %}
{% block title %}Iniciar sesión{% endblock %}
{% block content %}
<style>.errorlist{color:red;}</style>
<main role="main">
  <div class="container">
    <div class="row mt-3">
      <div class="col-md-9 mx-auto mb-5">
        <form action="" method="post">{% csrf_token %}
          <h3 class="mb-4">Iniciar sesión</h3>
          {% if form.non_field_errors %}
            <p style="color:red">Usuario o contraseña incorrectos, prueba de nuevo.</p>
          {% endif %}
          <p>
            <input type="text" name="username" autofocus maxlength="254" required
              id="id_username" class="form-control" placeholder="Nombre de usuario"/>
          </p>
          <p>
            <input type="password" name="password" required
              id="id_password" class="form-control" placeholder="Contraseña"/>
          </p>
          <p><input type="submit" class="btn btn-primary btn-block" value="Acceder"></p>
        </form>
      </div>
    </div>
  </div>
</main>
{% endblock %}
```

At this point we need to activate our app in setting.py, put at the top of the apps for give it priority.

```
# Application definition

INSTALLED_APPS = [
    'registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'pages.apps.PagesConfig',
    'ckeditor',
]
```

Go to your web browser and ¡wala! our login page is working on.

If you try login, it give us an error, it redirect us a profile for this user, and we need to redirect to an another page, and we need defineted it in setting.py.

```
# Auth redirect
LOGIN_REDIRECT_URL = 'home'
```

Try again and this work, it redirect the page.

## Closing the session

[Index](#Index)

In core/templates/core/base.html

```
            {% comment %} <ul class="navbar-nav">
              <li class="nav-item">
                <a class="nav-link" href="/admin/">
                  {% if request.user.is_staff %}Admin{% else %}Acceder{% endif %}
                </a>
              </li>
            </ul> {% endcomment %}
            <ul class="navbar-nav">
              {% if not request.user.is_authenticated %}
                <li class="nav-item">
                  <a class="nav-link" href="{% url 'login' %}">Acceder</a>
                </li>
              {% else %}
                <li class="nav-item">
                  <a class="nav-link" href="{% url 'logout' %}">Salir</a>
                </li>
               {% endif %}
            </ul>
```

In settings.py

```
# Auth redirect
LOGIN_REDIRECT_URL = 'pages:pages'
LOGOUT_REDIRECT_URL = 'pages:pages'
```

Try login and logout, see the result.

Has been so easy, ¿true?

## Register with CBV

[Index](#Index)

In urls.py general add this:

`    path('accounts/', include('registration.urls')),`

In registration/views.py

```
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'
```

Create a file urls.py in registrations:

```
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup")
]

```

Create a file in registration/templates/registration called signup.html

```
{% extends 'core/base.html' %}
{% load static %}
{% block title %}Registro{% endblock %}
{% block content %}
<style>.errorlist{color:red;}</style>
<main role="main">
  <div class="container">
    <div class="row mt-3">
      <div class="col-md-9 mx-auto mb-5">
        <form action="" method="post">{% csrf_token %}
          <h3 class="mb-4">Registro</h3>
          {{form.as_p}}
          <p><input type="submit" class="btn btn-primary btn-block" value="Acceder"></p>
        </form>
      </div>
    </div>
  </div>
</main>
{% endblock %}
```

Try in the web browser. And ¡Wala!

## Beauty Register with CBV

[Index](#Index)

In http://127.0.0.1:8000/accounts/signup/ with Ctr+U view-source

```
<main role="main">
  <div class="container">
    <div class="row mt-3">
      <div class="col-md-9 mx-auto mb-5">
        <form action="" method="post"><input type="hidden" name="csrfmiddlewaretoken" value="QjrXfQeESTfb3gA4zupoGxDfpUJ1qwv6WUmnaPxJGWnMBHAbQqnbBAJXLnD8L0IG">
          <h3 class="mb-4">Registro</h3>
          <p><label for="id_username">Username:</label> <input type="text" name="username" maxlength="150" autofocus required id="id_username"> <span class="helptext">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span></p>
<p><label for="id_password1">Password:</label> <input type="password" name="password1" required id="id_password1"> <span class="helptext"><ul><li>Your password can't be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can't be a commonly used password.</li><li>Your password can't be entirely numeric.</li></ul></span></p>
<p><label for="id_password2">Password confirmation:</label> <input type="password" name="password2" required id="id_password2"> <span class="helptext">Enter the same password as before, for verification.</span></p>
          <p><input type="submit" class="btn btn-primary btn-block" value="Acceder"></p>
        </form>
      </div>
    </div>
  </div>
</main>
```

Three inputs: username | password1 | password2

In registration/views.py

`from django import forms`

```
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # Modify in real time
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repite la contraseña'})
        return form
```

In registration/templates/registration/signup.html'

`use label = diplay=none`

In core/templates/core/base.html

```
{% if not request.user.is_authenticated %}
                <li class="nav-item">
                  <a class="nav-link" href="{% url 'login' %}">Acceder</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="{% url 'signup' %}">Registro</a>
                </li>
              {% else %}
                <li class="nav-item">
                  <a class="nav-link" href="{% url 'logout' %}">Salir</a>
                </li>
               {% endif %}
```

Well, so here we have a basic view about registration.

Let´s continue...

## Obligatory EMAIL

[Index](#Index)

In registrations create e new file called it forms.py

```
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres maximo y debe ser válido")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

```

In views.py registration

```
# from django.contrib.auth.forms import UserCreationForm # | THIS NOT BECAUSE WE EXTENDED A NEW VERSION IN REGISTRATIONS/FORMS.PY
from .forms import UserCreationFormWithEmail
```

```
class SignUpView(CreateView):
    # form_class = UserCreationForm # | THIS NOT UPDATE WITH EMAIL
    form_class = UserCreationFormWithEmail
```

`form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Direccion email'})`

## Unique Email

[Index](#Index)

In forms.py of registrations app

```
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya esta registrado, prueba con otro.")
        return email
```

## Password Forget

[Index](#Index)

In settings.py general add

```
# Emails Local
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, "send_emails")
else:
    # HERE REAL EMAIL FOR PRODUCTION
    pass
```

Go to  http://127.0.0.1:8000/accounts/password_reset/

And update the templates html, are in bases_files folder, copy in registration/templates/registrations/

Then you will see the new format of the form. Is so cool.

The original files are in django/django/contrib/admin/templates/registration

Send an email to pepipo5@pepito.com then the url will be http://127.0.0.1:8000/accounts/password_reset/done/

Now in the project there is a folder called it send_email where you will find the email for reset the password.

Try reset it is complete functional.

In registration/templates/registration/login.html after the form add

`

¿Ha olvidado su clave? Puede restaurarla [aquí]({% url 'password_reset' %})

`

## User Profile

[Index](#Index)

registration/models.py

```
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
```

registration/views.py

```
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(TemplateView):
    template_name = 'registration/profile_form.html'


```

registration/urls.py

```
from django.urls import path
from .views import SignUpView, ProfileUpdate

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),
]

```

general setting.py

```
# Auth redirect
# LOGIN_REDIRECT_URL = 'pages:pages'
```

For Pillow

```
# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

general urls.py

`from django.conf import settings`

```
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

create a file in templates/registration called it profile_form.html

```
{% extends 'core/base.html' %}
{% load static %}
{% block title %}Perfil{% endblock %}
{% block content %}

<main role="main">
  <div class="container">
    <div class="row mt-3 mb-5">
      <div class="col-md-9 mx-auto">
            <h3>Perfil</h3>
            <form action="" method="post">{% csrf_token %}
                    {{ form.as_p }}
                <div class="text-center">
                <input type="submit" class="btn btn-primary btn-block" value="Actualizar" />
                </div>
            </form>
      </div>
    </div>
  </div>
</main>
{% endblock %}
```

Wala! Is working on.

## Editable Profile

[Index](#Index)

First

`````python
python manage.py makemigrations registration
python manage.py migrate registration
`````

Transform TemplateView to UpdateView for our profile in registrations´s views.py

```
# from django.views.generic.base import TemplateView # UNNECESARY FOR PROFILE UPDATE 
from django.views.generic.edit import UpdateView
```

```
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
```

templates/registration/profile_form.html

````python
            <form action="" method="post" enctype="multipart/form-data">{% csrf_token %}```
````

Working on... Great!!!

## Beauty Profile Form

[Index](#Index)

registration/forms.py

`from .models import Profile`

```
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'row':3, 'placeholder':'Biografía'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace'}),
        }

```

registration/views.py

`from .forms import UserCreationFormWithEmail, ProfileForm`

```
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    # model = Profile # UNNECESSARY BECAUSE COMES FROM REGISTRATION´S FORMS.PY
    # fields = ['avatar', 'bio', 'link'] # UNNECESSARY BECAUSE COMES FROM REGISTRATION´S FORMS.PY
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        # RECOVER THE OBJECT WILL EDIT
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
```

profile_form.html

````python
<style>label{display:none}</style>
```
````

and change for

https://gist.github.com/gustavcaves/6a19ebca8b92d46bc0d85e5751e8711c

````python
{% extends 'core/base.html' %}
{% load static %}
{% block title %}Perfil{% endblock %}
{% block content %}
<style>.errorlist{color:red;} label{display:none}</style>
<main role="main">
  <div class="container">
    <div class="row mt-3">
      <div class="col-md-9 mx-auto mb-5">
        <form action="" method="post" enctype="multipart/form-data">{% csrf_token %}
          <div class="row">
            <!-- Previa del avatar -->
            <div class="col-md-2">
              {% if request.user.profile.avatar %}
                <img src="{{request.user.profile.avatar.url}}" class="img-fluid">
                <p class="mt-1">¿Borrar? <input type="checkbox" id="avatar-clear" name="avatar-clear" /></p>
              {% endif %}
            </div>
            <!-- Formulario -->
            <div class="col-md-10">
              <h3>Perfil</h3>
              <input type="file" name="avatar" class="form-control-file mt-3" id="id_avatar">
              {{ form.bio }}
              {{ form.link }}
              <input type="submit" class="btn btn-primary btn-block mt-3" value="Actualizar">
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</main>
{% endblock %}
```
````

At the of the profile_form.py

```
{% extends 'core/base.html' %}
{% load static %}
{% block title %}Perfil{% endblock %}
{% block content %}
<style>.errorlist{color:red;} label{display:none}</style>
<main role="main">
  <div class="container">
    <div class="row mt-3">
      <div class="col-md-9 mx-auto mb-5">
        <form action="" method="post" enctype="multipart/form-data">{% csrf_token %}
          <div class="row">
            <!-- Previa del avatar -->
            <div class="col-md-2">
              {% if request.user.profile.avatar %}
                <img src="{{request.user.profile.avatar.url}}" class="img-fluid">
                <p class="mt-1">¿Borrar? <input type="checkbox" id="avatar-clear" name="avatar-clear" /></p>
              {% else %}
                <img src="{% static 'registration/img/no-avatar.jpg' %}" class="img-fluid">
              {% endif %}
            </div>
            <!-- Formulario -->
            <div class="col-md-10">
              <h3>Perfil</h3>
              <input type="file" name="avatar" class="form-control-file mt-3" id="id_avatar">
              {{ form.bio }}
              {{ form.link }}
              <input type="submit" class="btn btn-primary btn-block mt-3" value="Actualizar">
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</main>
{% endblock %}
```

And again is working on ... Great!!

Let´s continue...

## Edit Email

[Index](#Index)

registration/forms.py

```
class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres maximo y debe ser válido")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.cleaned_data: # IS A LIST WHO SAVE ALL DATA CHANGED IN THE FORM
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya esta registrado, prueba con otro.")
        return email
```

registration/view.py

`from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm`

```
@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        # RECOVER THE OBJECT WILL EDIT
        return self.request.user

    def get_form(self, form_class=None):
  
        form = super(EmailUpdate, self).get_form()
        # Modify in real time
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Email'})
        return form
```

registration/urls.py

`from .views import SignUpView, ProfileUpdate, EmailUpdate`

`    path('profile/email/', EmailUpdate.as_view(), name="profile_email"),`

registratinon/templates/registration/profile_form-html

```
              <input type="email" value="{{request.user.email}}" class="form-control mt-3" readonly>
              <p class="mt-3">Si deseas editar tu email haz clic <a href="{% url 'profile_email' %}">aquí</a></p>
```

create a new file in registratinon/templates/registration called it profile_email_form.html

```
{% extends 'core/base.html' %}
{% load static %}
{% block title %}Email{% endblock %}
{% block content %}
<style>.errorlist{color:red;} label{display:none}</style>
<main role="main">
  <div class="container">
    <div class="row mt-3">
      <div class="col-md-9 mx-auto mb-5">
        <form action="" method="post">{% csrf_token %}
          <h3 class="mb-4">Email</h3>
          {{form.as_p}}
          <p><input type="submit" class="btn btn-primary btn-block" value="Actualizar"></p>
        </form>
      </div>
    </div>
  </div>
</main>
{% endblock %}
```

That all friends... Is so cool!!!

Thanks

## Intro To Signals

[Index](#Index)

Triggers

Registration/models.py

```
from django.dispatch import receiver
from django.db.models.signals import post_save

```

```
# DEFINE A SIGNAL CREATE A DEF FUCNTION
# TO TRIGGERT AUTOMATIC WE NEED CALLED IT, USE A DECORATOR @
@receiver(post_save, sender=User)
def ensure_profile_exist(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print ("Se acaba de crear un usuario y su perfil enlazado")
```

On shell

python manage.py shell

>>> from registration.models import Profile
>>> Profile.objects.get(user__username='pepito7')
>>> <Profile: Profile object (2)>
>>>
>>

## Intro to Unit Test

[Index](#Index)

registration/tests.py

```
from django.test import TestCase
from . models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test','test@test.com', 'test1234')

    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists, True)
```

CMD

````python
python manage.py test registration.tests
```
````

`````python
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
Se acaba de crear un usuario y su perfil enlazado
.
----------------------------------------------------------------------
Ran 1 test in 0.173s

OK
Destroying test database for alias 'default'...
```
````
`````

Is OK. Continue...

## Optimizing Avatar Storage

[Index](#Index)

registration/models.py

```
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename
```

`    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)`

## 9th App Public Profiles

[Index](#Index)

Copia esta app profiles en tu proyecto webplayground:

· En Windows ->	C:\CursoDjango\webplayground
· En Mac OS -> /Users/tu_usuario/Documents/CursoDjango/webplayground
· En Linux -> /home/tu_usuario/CursoDjango/webplayground

Para utilizarla debes hacer lo siguiente:

* [X] · Añade la app profiles en la lista INSTALLED_APPS de settings.py
* [X] · Configura las urls globales:

````python
from profiles.urls import profiles_patterns

# Paths de profiles

path('profiles/', include(profiles_patterns)),
```
````

* [X] · Añade la sección al menú superior en base.html:

`````python
    <li class="nav-item">
        <a class="nav-link" href="{% url 'profiles:list' %}">Perfiles</a>
    </li>
```
````
`````

## Pagination Of Results List View

[Index](#Index)

registration/model.py

```
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['user__username']
```

https://gist.github.com/gustavcaves/ee08435e472981b1d89c34b3325be1e2

profiles/templates/profiles/profile_list.html

````python
        <!-- Menú de paginación -->
          {% if is_paginated %}
            <nav aria-label="Page navigation">
              <ul class="pagination justify-content-center">
                {% if page_obj.has_previous %}
                  <li class="page-item ">
                    <a class="page-link" href="?page={{ page_obj.previous_page_number }}">«</a>
                  </li>
                {% else %}
                  <li class="page-item disabled">
                    <a class="page-link" href="#" tabindex="-1">«</a>
                  </li>
                {% endif %}
                {% for i in paginator.page_range %}
                  <li class="page-item {% if page_obj.number == i %}active{% endif %}">
                    <a class="page-link" href="?page={{ i }}">{{ i }}</a>
                  </li>
                {% endfor %}
                {% if page_obj.has_next %}
                  <li class="page-item ">
                    <a class="page-link" href="?page={{ page_obj.next_page_number }}">»</a>
                  </li>
                {% else %}
                  <li class="page-item disabled">
                    <a class="page-link" href="#" tabindex="-1">»</a>
                  </li>
                {% endif %}
              </ul>
            </nav>
          {% endif %}
```
````

UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list: <class 'registration.models.Profile'> QuerySet.
return self.paginator_class()

All Ok.

## 10 App Messenger

[Index](#Index)

````python
python manage.py startapp messenger
```
````

messenger/models.py

```
from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)
```

CMD

````python
python manage.py makemigrations messenger
python manage.py migrate messenger
```
````

Thats all Friends...

## TDD 1 Firts Test

[Index](#Index)

messenger/models.py

```
from django.test import TestCase

from django.contrib.auth.models import User
from .models import Thread, Message

# Create your tests here.
class ThreadTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user1', None, 'test1234')
        self.user2 = User.objects.create_user('user2', None, 'test1234')

        self.thread = Thread.objects.create()

    def test_add_user_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        self.assertEqual(len(self.thread.users.all()), 2)

```

CMD

````python
python manage.py test messenger.tests


Creating test database for alias 'default'...
System check identified no issues (0 silenced).
Se acaba de crear un usuario y su perfil enlazado
Se acaba de crear un usuario y su perfil enlazado
.
----------------------------------------------------------------------
Ran 1 test in 0.301s

OK
Destroying test database for alias 'default'...

```
````

registration/models.py

`        # print ("Se acaba de crear un usuario y su perfil enlazado")`


We can call only one test, try

````python
python manage.py test messenger.tests.ThreadTestCase
```
````

Or even past more

````python
python manage.py test messenger.tests.ThreadTestCase.test_add_user_to_thread
```
````

messenger/tests.py

```
    def test_filter_thread_by_users(self):
        self.thread.users.add(self.user1, self.user2)
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(self.thread, threads[0])
```

CMD

````python
python manage.py test messenger.tests.ThreadTestCase.test_filter_thread_by_users

Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.341s

OK
Destroying test database for alias 'default'...
```
````

```
from logging import setLoggerClass
from django.test import TestCase

from django.contrib.auth.models import User
from django.test.testcases import SerializeMixin
from .models import Thread, Message

# Create your tests here.
class ThreadTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user1', None, 'test1234')
        self.user2 = User.objects.create_user('user2', None, 'test1234')

        self.thread = Thread.objects.create()

    def test_add_user_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        self.assertEqual(len(self.thread.users.all()), 2)

    def test_filter_thread_by_users(self):
        self.thread.users.add(self.user1, self.user2)
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(self.thread, threads[0])

    def test_filter_non_existent_thread(self):
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(len(threads), 0)

    def test_add_messages_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        message1 = Message.objects.create(user=self.user1, content="Muy Buenas")
        message2 = Message.objects.create(user=self.user2, content="Hola")
        self.thread.messages.add(message1, message2)
        self.assertEqual(len(self.thread.messages.all()), 2)

        for message in self.thread.messages.all():
            print("({}): {}".format(message.user, message.content))
```

````python
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
(user1): Muy Buenas
(user2): Hola
....
----------------------------------------------------------------------
Ran 4 tests in 0.920s

OK
Destroying test database for alias 'default'...
```
````



This can´t considered TDD, all of this has given to us from django, we dont writing code here yet.







# Comments

[Index](#Index)

### wednesday, 10 march 2021 23:13

Mayby this comment could be useful, so I will used for write my progress in this theme CCBV.UK
