class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Relatorio:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        # Verifique se o objeto passado é uma instância da classe Venda.
        if isinstance(venda, Venda):
            self.vendas.append(venda)  # Adiciona a venda à lista
            
        

    def calcular_total_vendas(self):
        # Calcule o total de vendas baseado nas vendas adicionadas:
        total = sum(venda.quantidade * venda.valor for venda in self.vendas)
        return total

def main():
    relatorio = Relatorio()
    
    for i in range(3):  # Loop para adicionar três vendas, você pode ajustar esse número
        produto = input("")
        quantidade = int(input(""))
        valor = float(input(""))
        venda = Venda(produto, quantidade, valor)
        relatorio.adicionar_venda(venda)
    
    # Exiba o total de vendas usando o método calcular_total_vendas.
    total_vendas = relatorio.calcular_total_vendas()
    print(f"Total de Vendas: {total_vendas:.1f}")

if __name__ == "__main__":
    main()