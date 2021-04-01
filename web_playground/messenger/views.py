from django.shortcuts import redirect, render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views.generic import TemplateView

from .models import Message, Thread

from django.http import Http404, JsonResponse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.shortcuts import get_object_or_404, redirect

from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
@method_decorator(login_required, name="dispatch")
class ThreadList(TemplateView):
    # model = Thread
    # # Filtar un query set por defecto
    # def get_queryset(self):
    #     queryset = super(ThreadList, self).get_queryset()
    #     return queryset.filter(users=self.request.users)
    # # user.thread.all()
    template_name = "messenger/thread_list.html"

@method_decorator(login_required, name="dispatch")
class ThreadDetail(DetailView):
    model = Thread

    def get_object(self):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404
        return obj

# Que debemos devolver en una peticion asincrona? pues lo que queramos texto plano, un snipet html para inyectarlo directamente en la pagina o una estructura bien organizada en formato xml o json que podemos analizar para actuar en concecuencia. RECOMENDABLE USAR JSON
def add_message(request, pk): # import JsonResponse
    # print(request.GET) # Nos mostrara todos los paremtros que se envian por GET
    json_response = {'created':False} # Cuando añadamos un mensaje devolveremos una respuesta que es este json_response, si el mensaje se crea correctamente se cambiara False a True
    if request.user.is_authenticated:
        content = request.GET.get('content', None)
        if content:
            thread = get_object_or_404(Thread, pk=pk)
            message = Message.objects.create(user=request.user, content=content)
            thread.messages.add(message)
            json_response['created'] = True
            if len(thread.messages.all()) is 1:
                json_response['first'] = True
    else:
        raise Http404("User is not authenticated")
    
    return JsonResponse(json_response) # Y el automaticamente hace la convercion de un diccionario a un objeto json

@login_required
def start_thread(request, username):
    user = get_object_or_404(User, username=username)
    thread = Thread.objects.find_or_create(user, request.user)
    return redirect(reverse_lazy('messenger:detail', args=[thread.pk]))