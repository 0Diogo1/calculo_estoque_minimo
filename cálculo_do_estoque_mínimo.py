#cálculo de estoque mínimo da loja onde trabalho
nomedoproduto = input("Nome do produto: ")
consumoProduto = int(input("Quantidade vendida em um determinado período: "))
periodo = int(input("Período de venda em dias: "))
tempoReposição = int(input("Tempo de reposição do produto no estoque: "))
c = ""
while c != "Não":
    consumoMD = consumoProduto / periodo
    consumoMD = round(consumoMD)
    print(f'Consumo médio: {consumoMD} unidades por dia')
    estoqueminimo = consumoMD * tempoReposição
    estoqueminimo = round(estoqueminimo)
    print(f'Estoque mínimo: {estoqueminimo} unidades')
    c = input("Deseja calcular o estoque mínimo de mais algum produto?(SIM/NÃO): ").upper()
    if c == "SIM":
        nomedoproduto = input("Nome do produto: ")
        consumoProduto = int(input("Quantidade vendida em um determinado período: "))
        periodo = int(input("Período de venda em dias: "))
        tempoReposição = int(input("Tempo de reposição do produto no estoque: "))
    elif c == "NÃO":
        break
print("Fim do programa")


