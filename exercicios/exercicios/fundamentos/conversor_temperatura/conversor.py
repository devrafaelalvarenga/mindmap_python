'''
    Programa em Python que solicita ao usuário para digitar uma opção de conversão de temperatura, 
    e uma temperatura a ser convertida. 
    O programa então, devera imprimir uma mensagem informando o valor da temperatura convertido.
'''


def converter_celcius_para_fahrenheit(temperatura):
    """Função que converte a temperatura de celcius para fahrenheit

    Args:
        temperatura (_type_): Valor numerico informado pelo usuario para conversão

    Returns:
        _type_: Temperatura convertida de celcius para fahrenheit
    """
    return (temperatura * 9/5) + 32


def converter_fahrenheit_para_celcius(temperatura):
    """Função que converte a temperatura de fahrenheit para celcius 

    Args:
        temperatura (_type_): Valor numerico informado pelo usuario para conversão

    Returns:
        _type_: Temperatura convertida de fahrenheit para celcius 
    """
    return (temperatura - 32) * 5/9


def escolher_conversao():
    """Função que retorna a conversão escolhida pelo usuário

    Raises:
    ValueError: A opção desejada deve ser um número.
    ValueError: Opção desejada inexistente.

    Returns:
        _type_: Conversão escolhida pelo usuario sendo 1 para Celsius -> Fahrenheit ou 2 para Fahrenheit -> Celsius.
    """
    print('Bem vindo ao Conversor de Temperaturas. '
          'Escolha uma das opções: \n'
          '1 - Converter celcius para fahrenheit \n'
          '2 - Converter fahrenheit para celcius \n'
          '3 - Sair \n')

    tentativa = 0
    while tentativa < 3:
        try:
            opcao_desejada = input('Informe a opção desejada: ')
            if not opcao_desejada.isdigit():
                raise ValueError('A opção desejada deve ser um número.')
            opcao_desejada = int(opcao_desejada)
            if opcao_desejada not in range(1, 4):
                raise ValueError('Opção desejada inexistente.')
            elif opcao_desejada == 3:
                print('Programa Encerrado.')
                exit()
        except Exception as e:
            print(e)
            tentativa += 1
            if tentativa == 3:
                print('Número de tentativas excedido. Tente novamente.')
            else:
                print(f'Tentativas restantes: {3 - tentativa}')
        else:
            return opcao_desejada


def captar_temperatura():
    """Função que capta a temperatura infromada pelo usuario para realizar a conversão

    Raises:
        ValueError: A temperatura deve ser um numero.

    Returns:
        _type_: Temperatura informada para conversão.
    """
    tentativa = 0
    while tentativa < 3:
        try:
            temperatura = input('Informe a temperatura para conversão: ')
            if not temperatura.isdigit():
                raise ValueError('A temperatura deve ser um numero.')
            temperatura = float(temperatura)
        except Exception as e:
            print(e)
            tentativa += 1
            if tentativa == 3:
                print('Número de tentativas excedido. Tente novamente.')
            else:
                print(f'Tentativas restantes: {3 - tentativa}')
        else:
            return temperatura


def conversor_de_temperaturas(escolha, temperatura):
    """Função que converte a temperatura informada a partir da opção de conversão selecionada pelo usuario 

    Args:
        escolha (_type_): retorno da função escolher_conversao()
        temperatura (_type_): retorno da função captar_temperatura()

    Raises:
        ValueError: Escolha inválida. Use 1 para Celsius -> Fahrenheit ou 2 para Fahrenheit -> Celsius.

    Returns:
        _type_: Temperatura convertida a partir da temperatura informada e da opção de conversão selecionada pelo usuario 
    """
    if escolha == 1:
        return converter_celcius_para_fahrenheit(temperatura)
    elif escolha == 2:
        return converter_fahrenheit_para_celcius(temperatura)
    else:
        raise ValueError(
            "Escolha inválida. Use 1 para Celsius -> Fahrenheit ou 2 para Fahrenheit -> Celsius.")


if __name__ == '__main__':
    escolha = escolher_conversao()
    temperatura = captar_temperatura()
    temperatura_convertida = conversor_de_temperaturas(
        escolha=escolha, temperatura=temperatura)

    if escolha == 1:
        print(
            f'A conversão de {temperatura}˚Celsius para Fahrenheit é {temperatura_convertida}˚F.')
    elif escolha == 2:
        print(
            f'A conversão de {temperatura}˚ Fahrenheit para Celsius é {temperatura_convertida}˚C.')
