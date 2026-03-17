from django.shortcuts import render

def base_view(request):
    """
    Renderiza a pagina de teste com os componentes do Bootstrap customizado.
    """
    return render(request, 'app_teste/base.html')