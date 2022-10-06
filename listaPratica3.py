#exercicio 1
for numero in range (1, 51):
    print(numero)

#exercicio 2
for numero in range (1, 101):
    if numero % 2 == 0:
        print(numero)

#exercicio 3
# o usuario nao pode digitar um numero diferente
numero = int(input("Digite um numero de 1 a 10: "))

while numero < 1 or numero > 10:
    numero = int(input("Digite um numero de 1 a 10: "))

for valor in range(1, 11):
    print(valor * numero)

#exercicio 4
somaIdades = 0
for idade in range(1, 11):
    valor = float(input("Digite uma idade: "))
    somaIdades = somaIdades + valor
print("A média desses valores é " + str(somaIdades/10))

#exercicio 5
pares = 0
impares = 0
for numero in range(1, 11):
    numeros = int(input("Digite "))



