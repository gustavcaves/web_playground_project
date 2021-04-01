from django.urls import path
from .views import ThreadList, ThreadDetail, add_message, start_thread

messenger_patterns = ([
    path('', ThreadList.as_view(), name="list"),
    path('thread/<int:pk>/', ThreadDetail.as_view(), name="detail"),
    path('thread/<int:pk>/add/', add_message, name="add"),
    # Que debemos devolver en una peticion asincrona? pues lo que queramos texto plano, un snipet html para inyectarlo directamente en la pagina o una estructura bien organizada en formato xml o json que podemos analizar para actuar en concecuencia. RECOMENDABLE USAR JSON
    path('thread/start/<username>/', start_thread, name="start"),
], "messenger")