import unicodedata

lista = [
    "  leite  ", "pão", "ARROZ", "Feijão", "pão", "chocolate", "refrigerante",
    "feijao", "arroz ", "Cerveja", "água", "leite", "macarrão ", " GuarANÁ  ", "lImão",
    "BATATA", "peixE", "Vinagre    "
]


def normalizar_lista(lista: list) -> list:
    """
    Normaliza os itens de uma lista de strings, removendo espaços extras, 
    convertendo para minúsculas e removendo acentos. Também remove dados duplicados.

    Args:
        lista (list): Lista de strings a ser normalizada.

    Raises:
        ValueError: Se a lista contiver números.
        ValueError: Se a lista estiver vazia após a normalização.

    Returns:
        list: Lista normalizada e sem dados duplicados.
    """
    try:
        lista_atualizada: list = []
        for i in lista:
            if i.isdigit():
                raise ValueError('A  lista não pode conter numeros.')
            else:
                item: str = unicodedata.normalize('NFKD', i.strip().lower()).encode(
                    'ASCII', 'ignore').decode('ASCII')
            lista_atualizada.append(item)
        lista_atualizada = set(lista_atualizada)
        if len(lista_atualizada) == 0:
            raise ValueError('A lista esta vazia.')
    except Exception as e:
        print(e)
        exit()
    else:
        print(lista_atualizada)


if __name__ == '__main__':
    normalizar_lista(lista=lista)
