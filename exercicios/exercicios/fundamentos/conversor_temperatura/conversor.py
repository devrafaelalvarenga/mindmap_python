'''
    Programa em Python que solicita ao usuário para digitar uma opção de conversão, 
    e uma temperatura a ser convertida. 
    O programa então, devera imprimir uma mensagem informando o valor da temperatura convertido.
'''


def converter_celcius_para_fahrenheit(celcius):
    """_summary_

    Args:
        celcius (_type_): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    return (celcius * 9/5) + 32


def converter_fahrenheit_para_celcius(fahrenheit):
    """_summary_

    Args:
        fahrenheit (_type_): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    return (fahrenheit - 32) * 5/9


def escolher_conversao():
    """_summary_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
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
    pass


def conversor_de_temperaturas():
    pass


if __name__ == '__main__':
    escolher_conversao()
