import unicodedata


def criar_lista_de_compra() -> dict:
    """
        Cria uma lista de compras categorizada com base na entrada do usuário.

        A função permite ao usuário adicionar itens a categorias predefinidas
        ('alimento', 'higiene', 'limpeza', 'outros') ou encerrar o processo.
        Ela valida a entrada do usuário e garante que os itens sejam únicos dentro de cada categoria.

    Raises:
        Exception: Se a entrada da categoria for inválida (não for um dígito ou estiver fora do intervalo).
        Exception: Se a entrada do item for inválida (contiver caracteres não alfabéticos).
        ValueError: Se o usuário exceder o número máximo de tentativas inválidas (3).

    Returns:    
        dict: Um dicionário contendo a lista de compras categorizada.
        As chaves são os nomes das categorias ('alimento', 'higiene', 'limpeza', 'outros'),
        e os valores são listas de itens únicos adicionados a cada categoria.
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
                for categoria, lista in lista_de_compra.items():
                    lista_de_compra[categoria] = list(set(lista))
                print(lista_de_compra)
                break

            item: str = input(
                f'Informe um item para anexar na lista da categoria: ')

            item: str = unicodedata.normalize('NFKD', item).encode(
                'ASCII', 'ignore').decode('ASCII').strip().lower()

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


if __name__ == '__main__':
    criar_lista_de_compra()
