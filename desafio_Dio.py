""" Você está trabalhando em um projeto de Power BI onde precisa analisar dados 
de vendas mensais de uma empresa. 
Em Power BI, os dados são frequentemente representados em tabelas,
e você precisa calcular alguns indicadores básicos. 
Sua tarefa é calcular o total de vendas e a média mensal de vendas que serão usados para gerar relatórios e gráficos no Power BI, além de criar uma lista em Python para calcular o total de vendas e a sua média mensal.

Detalhamento:

Na função obter_entrada_vendas() você deverá:

Utilizar o método split(',') para dividir a string de entrada em elementos separados por vírgula, criando assim uma lista de strings.

Aplique a função map(int, ...) para converter cada elemento dessa lista de strings em um inteiro.

Usar a função list() para converter o objeto map resultante em uma lista de inteiros.

Essa lista de inteiros representará os valores de vendas que serão utilizados para calcular o total e a média mensal de vendas em outra função.

Entrada
Uma lista com 12 números inteiros, cada um representando o número de vendas realizadas em um mês do ano.

Saída
Um único número inteiro representando o total de vendas e um número decimal representando a média mensal de vendas, separados por um espaço.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
120, 150, 170, 130, 200, 250, 180, 220, 210, 160, 140, 190	2120, 176.67
10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120	780, 65.00
5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60	390, 32.50
Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código
"""


def analise_vendas(vendas):
    
    total_vendas = sum(vendas)
    # TODO: Calcule o total de vendas e realize a média mensal:
    
    media_vendas = sum(vendas) / len(vendas)
    return f"{total_vendas}, {media_vendas:.2f}"


def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input("digite as vendas no mês separados por vírgula: ")
    # TODO: Converta a entrada em uma lista de inteiros:
    vendas = [int(i.strip()) for i in entrada.split(',')]  # Converte para lista de inteiros
    
    return vendas


vendas = obter_entrada_vendas()


print(analise_vendas(vendas))


    






