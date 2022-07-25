from dataclasses import replace


def formata_preco(val):
    try:
        import locale
        valor_int = float(val)
        locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
        valor_formatado = locale.currency(valor_int, grouping=True)
        return valor_formatado
    except ValueError:
        # Trate o erro
        raise

    # if __name__ == "__main__":
    # preco = '2500.28'
    # print(formata_preco(preco))

    # return f'R$ {val:,.2f}'
