# --- SCRIPT: CONVERSOR DE TEMPERATURA ---
# Desenvolvido para a equipa de Suporte a Cálculos da DataCode Solutions

# O input recebe o dado como texto e o float converte-o para número decimal (casting)
temperatura_celsius = float(input("Digite a temperatura em graus Celsius (°C): "))

# Processamento: aplicação da fórmula matemática adaptada para a sintaxe Python
temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32

# Saída de dados: exibição do resultado utilizando f-string para maior legibilidade
print(f"A temperatura convertida é {temperatura_fahrenheit} graus Fahrenheit.")