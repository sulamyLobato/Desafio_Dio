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


    






