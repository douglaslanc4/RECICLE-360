from django.shortcuts import render
from django.http import HttpResponse
from .models import recolhe,ServicosAbertos 

import base64

def index(request):
    return render(request, 'index.html')

def solicitacao(request):
    return render(request, 'solicitacao.html')

# Renamed view function to avoid conflict with the model
def solicitacoes(request):
    solicitacoes = recolhe.objects.all()
    
    # Pass the records to the template
    context = {
        'solicitacoes': solicitacoes
    }
    return render(request, 'recolhe.html', context)

def quemsomos(request):
    return render(request, 'quemsomos.html')

def encerra(request):
    solicitacoes = recolhe.objects.all()
    
    # Pass the records to the template
    context = {
        'solicitacoes': solicitacoes
    }
    return render(request, 'encerra.html', context)

def envia(request):
    if request.method == 'POST':
        # Retrieve form data
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        data_solicitacao = request.POST.get('data_solicitacao')
        descricao = request.POST.get('descricao')

        # Create a new instance of `recolhe`
        solicitacao = recolhe(
            nome=nome,
            endereco=endereco,
            telefone=telefone,
            email=email,
            data_solicitacao=data_solicitacao,
            descricao=descricao,
            status="Pendente"  # Optional default value
        )
        solicitacao.save()  # Save the instance to the database

        # Redirect to a success page or render a success message
        return render(request, 'envia.html')  # Success template
    
    return HttpResponse("Invalid request method", status=405)

def exclui(request):
    if request.method == 'POST':
        # Get the ID of the entry to delete from the request POST data
        id_to_delete = request.POST.get('id')

        # Retrieve the entry from the database using the ID
        entry_to_delete = recolhe.objects.get(pk=id_to_delete)

        # Delete the entry
        entry_to_delete.delete()

        # Redirect to the confirmation page
        return render(request, 'exclui.html')

    # If the request method is not POST, redirect to the home page
    return redirect('/')

def abertas(request):
   # Ensure you're using the correct model
   solicitacoes_abertas = recolhe.objects.filter(status="Pendente")
   context = {'solicitacoes_abertas': solicitacoes_abertas}
   return render(request, 'abertas.html', context)

def atribui(request):
    if request.method == 'POST':
        solicitacao_id = request.POST.get('solicitacao_id')
        nome = request.POST.get('nome')
        contato = request.POST.get('contato')

        try:
            solicitacao = recolhe.objects.get(pk=solicitacao_id)
        except recolhe.DoesNotExist:
            return HttpResponse("Solicitação não encontrada", status=404)

        solicitacao.status = "Em Andamento"
        solicitacao.save()

        servico = ServicosAbertos(
            solicitacao_id=solicitacao_id,
            nome=nome,
            contato=contato,
        )
        servico.save()

        return render(request,'atribui.html')

    return HttpResponse("Invalid request method", status=500)
