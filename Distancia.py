# 1. Entradas de dados (padrão snake_case com letras minúsculas)
distancia = float(input("Digite a distância percorrida em km (apenas números): "))
consumo_medio = float(input("Quantos km o seu carro faz por litro? "))
preco_combustivel = float(input("Digite o preço do combustível no posto: "))

# 2. Processamento (A matemática correta)
# Quantos litros vou precisar para a viagem toda?
litros_necessarios = distancia / consumo_medio

# Quanto isso vai me custar em dinheiro?
custo_total = litros_necessarios * preco_combustivel

# 3. Saída de dados
print(f"Você vai precisar de: {litros_necessarios:.2f} litros de combustível.")
print(f"O custo total da viagem será de: R$ {custo_total:.2f}")