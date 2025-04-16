'''
    Escreva um programa em Python que solicita ao usuário para digitar seu nome, 
    o valor do seu salário mensal e o valor do bônus que recebeu. 
    O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e 
    informando o valor do salário em comparação com o bônus recebido.
    '''


def coletar_nome() -> str:
    """Função que coleta o nome do usuario. 
       Programa é encerrado após três tentativas inválidas.

    Raises:
        ValueError: Nome não pode conter digitos não alfabeticos ou espaços.

    Returns:
        str: Função retorna o nome informado pelo usuário
    """
    validacao: int = 0
    while validacao < 3:
        try:
            nome_usuario: str = input('Digite o seu nome: ').title()
            if nome_usuario.isalpha() == False:
                raise ValueError(
                    'Nome não pode conter digitos não alfabeticos ou espaços.')
        except ValueError as e:
            print(e)
            validacao += 1
            if validacao == 3:
                print(f'Tente novamente')
                exit()
            else:
                print(f'Tentativa: {validacao}')
        else:
            return nome_usuario


if __name__ == '__main__':
    coletar_nome()
