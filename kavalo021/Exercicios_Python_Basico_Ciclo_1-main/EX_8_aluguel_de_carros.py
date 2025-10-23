# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------


dias = float(input("digite a quantidade de dias com o carro"))
km = float(input("digite digite a kilometragem"))
diaria = 500
total_dias = dias * diaria
total_km =km * 500
aluguel_total = total_dias + total_km

print(f"voce andou {km},e voce ficou com o carro {dias} , entao o total a pagar é {aluguel_total}")