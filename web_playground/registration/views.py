# from django.contrib.auth.forms import UserCreationForm # | THIS NOT BECAUSE WE EXTENDED A NEW VERSION IN REGISTRATIONS/FORMS.PY
from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy

from django import forms

# from django.views.generic.base import TemplateView # UNNECESARY FOR PROFILE UPDATE 
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Profile # FOR MODEL IN CLASS VIEW UPDATE VIEW

# Create your views here.

class SignUpView(CreateView):
    # form_class = UserCreationForm # | THIS NOT UPDATE WITH EMAIL
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # Modify in real time
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Direccion email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repite la contraseña'})
        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['avatar', 'bio', 'link']
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        # RECOVER THE OBJECT WILL EDIT
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile