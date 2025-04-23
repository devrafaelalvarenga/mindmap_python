from conversor import converter_celcius_para_fahrenheit, converter_fahrenheit_para_celcius, captar_temperatura, conversor_de_temperaturas, escolher_conversao

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
