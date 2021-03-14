from django.urls import path
from . import views

pages_patterns = ([
    path('', views.PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', views.PageDetailView.as_view(), name='page'),
    path('create/', views.PageCreate.as_view(), name='create'),
    path('update/<int:pk>', views.PageUpdate.as_view(), name='update'),
], 'pages')