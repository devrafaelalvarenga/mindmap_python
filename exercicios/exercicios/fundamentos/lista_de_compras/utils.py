import unicodedata

lista = [
    "  leite  ", "pão", "ARROZ", "Feijão", "pão", "chocolate", "refrigerante",
    "feijao", "arroz ", "Cerveja", "água", "leite", "macarrão ", " GuarANÁ  ", "lImão",
    "BATATA", "peixE", "Vinagre    "
]


def criar_lista_de_compra() -> dict:
    """    
    Cria uma lista de compras organizada por categorias: alimento, higiene, limpeza e outros.
    Permite ao usuário adicionar itens a cada categoria ou encerrar o programa.

    Raises:
        Exception: Se a categoria informada não for válida.
        Exception: Se o item informado não for válido.
        Exception: Se o número de tentativas exceder o limite permitido.
        ValueError: Se o programa for encerrado sem itens adicionados.

    Returns:
        dict: Um dicionário contendo as categorias como chaves e os itens adicionados como valores.
    """
    lista_de_compra: dict = {'alimento': [],
                             'higiene': [], 'limpeza': [], 'outros': []}
    tentativa: int = 0
    itens_incluidos: int = 0
    while tentativa <= 3:
        try:
            print('Informe uma categoria para anexar um item a lista de compra.')
            categoria: str = input(
                '1 -alimento | 2 -higiene | 3 -limpeza | 4 -outros | 5 -para encerrar: ')

            if not categoria.isdigit():
                raise Exception(
                    'Categoria invalida.')

            categoria: int = int(categoria)
            if categoria not in range(1, 6):
                raise Exception(
                    'Categoria inválida. Por favor, escolha uma categoria válida.')
            elif categoria == 5 and itens_incluidos == 0:
                print('Programa encerrado. Lista vazia.')
                break
            elif categoria == 5 and itens_incluidos > 0:
                return lista_de_compra

            item: str = input(
                f'Informe um item para anexar na lista da categoria: ').strip().lower()

            if not item.replace(" ", "").isalpha():
                raise Exception('Item invalido.')

            if categoria == 1:
                lista_de_compra["alimento"].append(item)
                itens_incluidos += 1
            elif categoria == 2:
                lista_de_compra["higiene"].append(item)
                itens_incluidos += 1
            elif categoria == 3:
                lista_de_compra["limpeza"].append(item)
                itens_incluidos += 1
            elif categoria == 4:
                lista_de_compra["outros"].append(item)
                itens_incluidos += 1

        except Exception as e:
            print(e)
            tentativa += 1
            if tentativa == 3:
                print('Tentativas excedidas, inicie novamente.')
                exit()
            else:
                print(f'Tentativas restantes: {3 - tentativa}')

# alterar a funcao abaixo visto que agora a lista de comra esta dentro de um dicionario


def normalizar_lista_de_compra(lista: list) -> list:
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
                raise ValueError('A lista não pode conter numeros.')
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
    criar_lista_de_compra()
    # normalizar_lista_de_compra(lista=lista)
