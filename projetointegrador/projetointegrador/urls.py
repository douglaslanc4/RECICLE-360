"""
URL configuration for projetointegrador project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recicle360 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('solicitacao/', views.solicitacao, name='solicitacao'),
    path('quemsomos/', views.quemsomos, name='quemsomos'),
    path('recolhe/', views.solicitacoes, name='recolhe'),
    path('solicitacao/envia', views.envia, name='envia'),
    path('abertas/', views.abertas, name='abertas'),
    path('encerra/', views.encerra, name='encerra'),
    path('atribui/', views.atribui, name='atribui'),
    path('exclui/', views.exclui, name='exclui'),
    
    
]
