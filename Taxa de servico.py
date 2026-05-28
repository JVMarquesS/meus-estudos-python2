# Solicitando o valor consumido
valor_consumido = float(input("Digite o total do valor consumido: "))

# Calculando a taxa (10%)
taxa_servico = valor_consumido * 0.10

# Calculando o total geral
valor_total = valor_consumido + taxa_servico

# Exibindo os resultados formatados
print(f"A taxa de serviço é: R$ {taxa_servico:.2f}")
print(f"O valor total da conta com os 10% é: R$ {valor_total:.2f}")