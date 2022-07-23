from django.template import Library
from uteis import uteis


register = Library()


@register.filter
def formata_preco(val):
    return uteis.formata_preco(val)
