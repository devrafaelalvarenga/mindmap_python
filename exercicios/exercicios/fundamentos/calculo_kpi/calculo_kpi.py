'''
    Escreva um programa em Python que solicita ao usuário para digitar seu nome, 
    o valor do seu salário mensal e o valor do bônus que recebeu. 
    O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e 
    informando o valor do salário em comparação com o bônus recebido.
'''


def coletar_nome() -> str:
    """Função que coleta o nome informado pelo usuario. 
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
                print(f'Número de tentativas excedido. Tente novamente')
                exit()
            else:
                print(f'Tentativas restantes: {3 - validacao}')
        else:
            return nome_usuario


def coletar_salario() -> float:
    """Função que coleta o valor do salário informado pelo usuário. 
       Programa é encerrado após três tentativas inválidas.

    Raises:
        ValueError: Informe um valor valido e "inteiro" para o salário.
        ValueError: Informe um valor valido e maior que zero para o salário.

    Returns:
        float: Função retorna o valor do salário informado pelo usuário
    """
    validacao: int = 0
    while validacao < 3:
        try:
            salario_usuario = float(
                input('Digite o valor "inteiro" seu salário: R$'))
            if salario_usuario.is_integer() == False:
                raise ValueError(
                    'Informe um valor valido e "inteiro" para o salário.')
            elif salario_usuario <= 0:
                raise ValueError(
                    'Informe um valor valido e maior que zero para o salário.')
        except Exception as e:
            print(e)
            validacao += 1
            if validacao == 3:
                print(f'Número de tentativas excedido. Tente novamente')
                exit()
            else:
                print(f'Tentativas restantes: {3 - validacao}')
        else:
            return salario_usuario


def identificar_desempenho() -> float:
    """Função que gera o multiplicador utilizado no cálculo do bonus do usuário.
       Programa é encerrado após três tentativas inválidas.

    Raises:
        ValueError: Informe um nível de desempenho válido (um número entre 1 e 5).

    Returns:
        float: Valor do multiplicador utilizado no cálculo do bonus do usuário
    """
    validacao: int = 0
    while validacao < 3:
        try:
            entrada: str = input(
                'Informe o número que represente o nível de desempenho informado na sua avaliação: 1-Excelente | 2-Muito Bom | 3-Bom | 4-Regular | 5-Insatisfatório : ')
            if entrada.isnumeric() == False:
                raise ValueError(
                    'Informe um nível de desempenho válido (um número entre 1 e 5).')
            elif int(entrada) not in range(1, 6):
                raise ValueError(
                    'Informe um nível de desempenho válido (um número entre 1 e 5).')

            nivel_de_desempenho = int(entrada)
            if nivel_de_desempenho == 1:
                multiplicador = 2.0
            elif nivel_de_desempenho == 2:
                multiplicador = 1.5
            elif nivel_de_desempenho == 3:
                multiplicador = 1.0
            elif nivel_de_desempenho == 4:
                multiplicador = 0.5
            elif nivel_de_desempenho == 5:
                multiplicador = 0.0

        except Exception as e:
            print(e)
            validacao += 1
            if validacao == 3:
                print(f'Número de tentativas excedido. Tente novamente')
                exit()
            else:
                print(f'Tentativas restantes: {3 - validacao}')
        else:
            return multiplicador


def calcular_kpi(salario_usuario: float, multiplicador: float) -> float:
    """Função que calcula o bonus do usuário.

    Args:
        salario_usuario (float): Salario declarado pelo usuário
        multiplicador (float): Valor definido a partir do resultado da avaliação de desempenho declarada pelo usuario

    Returns:
        float: Valor do bonus do usuario
    """
    bonus_total: float = salario_usuario * multiplicador
    return bonus_total


if __name__ == '__main__':
    nome_usuario = coletar_nome()
    salario_usuario = coletar_salario()
    multiplicador = identificar_desempenho()
    bonus_total = calcular_kpi(salario_usuario=salario_usuario,
                               multiplicador=multiplicador)

    print(
        f'O valor calculado para o bonus do funcionário {nome_usuario} é R$ {bonus_total:.2f}.')
