from calculo_kpi import coletar_nome, coletar_salario, identificar_desempenho, calcular_kpi

nome_usuario = coletar_nome()
salario_usuario = coletar_salario()
multiplicador = identificar_desempenho()
bonus_total = calcular_kpi(salario_usuario=salario_usuario,
                           multiplicador=multiplicador)

print(
    f'O valor calculado para o bonus do funcionário {nome_usuario} é R$ {bonus_total:.2f}.')
