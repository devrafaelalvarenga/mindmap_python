📦 Cenário:
Uma lista de compras em texto,  mal formatada, com erros de digitação e duplicatas.

🛠️ Tarefas a serem desenvolvidas (com foco funcional)
1. Normalizar os dados
Remover espaços em branco.

2. Colocar tudo em minúsculas.

3. Eliminar acentos (opcional).

4. Remover duplicatas
Usar set() ou lógica funcional pura.

5. Filtrar itens não saudáveis
Criar uma função é_saudavel(item) que filtra alimentos como refrigerante, chocolate, cerveja, etc.

6. Aplicar preços
Simular um dicionário com preços dos produtos.

7. Calcular total de gasto
Usar reduce para somar os valores dos itens.

8. Sugestão de economia
Criar uma versão da lista excluindo os itens não saudáveis e mostrar quanto seria economizado.

9. Gerar relatório final
Mostre:

Lista limpa e formatada

Itens saudáveis

Itens não saudáveis

Total real

Total saudável

Economia

🚀 Extras (opcional)
Usar functools.partial para funções especializadas.

Criar funções curried (soma(a)(b)).

Criar um pipeline de transformação.

Exportar para .json ou .csv.

lista:
entrada = [
    "  leite  ", "pão", "ARROZ", "Feijão", "pão", "chocolate", "refrigerante", 
    "feijao", "arroz ", "Cerveja", "água", "leite"
]

precos:
precos = {
    "leite": 4.5,
    "pão": 1.2,
    "arroz": 5.0,
    "feijão": 4.0,
    "água": 2.0,
    "chocolate": 6.0,
    "refrigerante": 7.0,
    "cerveja": 5.5
}

