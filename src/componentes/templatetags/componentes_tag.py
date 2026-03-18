"""
Módulo de Template Tags para Componentes de UI.

Este módulo disponibiliza tags de inclusão customizadas para facilitar a
reutilização de componentes de interface (como cards do Bootstrap 5)
dentro dos templates do Django.
"""

from typing import Any
from django import template

register = template.Library()

@register.inclusion_tag('componentes/card.html')
def card(
    card_img_top: str | None = None, 
    alt: str = "Imagem", 
    card_title: str | None = None, 
    card_subtitle: str | None = None, 
    card_text: str | None = None, 
    links: list[dict[str, str]] | None = None, 
    style: str = "width: 18rem;", 
    extra_class: str = ""
) -> dict[str, Any]:
    """
    Gera o contexto para um Card do Bootstrap 5.

    Recebe parâmetros opcionais para preencher as seções de um card HTML e
    suporta uma lista dinâmica de links para o rodapé do corpo do card.

    :param card_img_top: URL da imagem a ser exibida no topo do card.
    :type card_img_top: str, opcional
    :param alt: Texto alternativo de acessibilidade para a imagem.
    :type alt: str, opcional
    :param card_title: Título principal do card.
    :type card_title: str, opcional
    :param card_subtitle: Subtítulo do card.
    :type card_subtitle: str, opcional
    :param card_text: Conteúdo textual principal do card.
    :type card_text: str, opcional
    :param links: Lista de dicionários contendo chaves 'url', 'class' e 'text'.
    :type links: list[dict[str, str]], opcional
    :param style: Regras de CSS inline aplicadas ao container principal.
    :type style: str, opcional
    :param extra_class: Classes CSS adicionais para o container principal.
    :type extra_class: str, opcional
    :return: Dicionário de contexto que será injetado no template 'card.html'.
    :rtype: dict[str, Any]
    """
    
    # Previne erros caso a lista de links seja passada como None
    links_seguros = links or []

    return {
        'card_img_top': card_img_top,
        'alt': alt,
        'card_title': card_title,
        'card_subtitle': card_subtitle,
        'card_text': card_text,
        'links': links_seguros, 
        'style': style,
        'extra_class': extra_class,
    }