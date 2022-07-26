from django.template import Library
from uteis import formatar_preco


register = Library()


@register.filter
def formata_preco(val):
    return formatar_preco.formata_preco(val)
