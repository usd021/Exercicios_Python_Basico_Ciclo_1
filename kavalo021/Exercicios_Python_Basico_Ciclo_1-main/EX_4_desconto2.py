# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite a porcentagem de desconto: "))  


valor_final = preco - (preco * desconto / 100)


print(f"Produto: {produto()}")
print(f"Preço: {preco}")
print(f"Porcentagem de desconto: {desconto}")
print(f"O produto()) com {desconto}% de desconto custará R$ {valor_final}")