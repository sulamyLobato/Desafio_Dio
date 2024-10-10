class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []  # Lista de vendas

    # Método para adicionar uma venda à lista de vendas    
    def adicionar_venda(self, venda):
        self.vendas.append(venda)

    # Método para calcular e retornar o total das vendas
    def total_vendas(self):
        total = sum(x.valor for x in self.vendas)
        return total

def main():
    categorias = []

    for i in range(2):
        nome_categoria = input()
        categoria = Categoria(nome_categoria)

        for j in range(2): 
            entrada_venda = input()
            produto, quantidade, valor = entrada_venda.split(',')
            quantidade = int(quantidade.strip())
            valor = float(valor.strip())

            venda = Venda(produto.strip(), quantidade, valor)
            # Adicionando a venda à categoria 
            categoria.adicionar_venda(venda)

        categorias.append(categoria)
    
    # Exibindo os totais de vendas 
    for categoria in categorias:
        print(f"Vendas em {categoria.nome}: {categoria.total_vendas():.1f}")

if __name__ == "__main__":
    main()
