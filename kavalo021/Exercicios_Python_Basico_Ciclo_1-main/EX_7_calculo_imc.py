# Escreva um código que pede ao usuário a altura e o peso e faça o cálculo do IMC (Índice de massa corporal) do usuário.
# Dica:
# Para calcular o IMC você deve dividir o peso pela altura ao quadrado
# imc = peso / (altura ** 2)


# OUTPUT ESPERADO:

# Digite sua altura: 1.78
# Digite seu peso: 85
# O seu IMC é: 26.83

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------


nome = input("digite seu nome:")
altura = float(input("digite sua altura: "))
peso = float(input("digite sua peso: "))

imc = peso / (altura ** 2)
imc_arredondado = round(imc, 2)

print(f"o seu imc é {imc_arredondado}")