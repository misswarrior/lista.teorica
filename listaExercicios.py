anoNascimento = int(input("Digite seu ano de nascimento"))
anoAtual = 2032
idadeFuturo = anoAtual - anoNascimento
print("Em 2032 voce terá:" + str(idadeFuturo) + "anos")

seuNumero = int(input("Digite um número"))
sucessor = int(seuNumero) + 1
antecessor = int(seuNumero) - 1
print("O antecessor desse número é " + str(antecessor))
print("O sucessor desse número é " + str(sucessor))

raioCirculo = int(input("Digite o raio da circunferencia"))
diametroCirculo = raioCirculo * raioCirculo
areaCirculo = 2 * 3.14 * raioCirculo
print("O diametro da circunferencia é: " + str(diametroCirculo))
print("A área da circunferencia é: " + str(areaCirculo))

seuSalario = float(input("Digite seu sálario"))
salarioMinimo = 1212
quantidadeSalarios = seuSalario / salarioMinimo
print("Voce recebe " + str(quantidadeSalarios) + " salários mínimos")

precoProduto = float(input("Digite o preço do produto: "))
parcelas = float(input("Digite em quantas parcelas você deseja pagar: 1, 2 ou 3: "))
if parcelas == 1:
    print("Você pagará " + str(precoProduto * 0.95) + " reais")
elif parcelas == 2:
    print("Você pagará " + str(precoProduto/2) + " reais")
elif parcelas == 3:
    print("Você pagará " + str(precoProduto * 1.05) + " reais")

primeiroCateto = float(input("Digite o primeiro cateto: "))
segundoCateto = float(input("Digite o segundo cateto: "))
hipotenusaTriangulo = (primeiroCateto * primeiroCateto) + (segundoCateto * segundoCateto)
import math
print("A hipotenusa desse triângulo é: " + str(math.sqrt(hipotenusaTriangulo)))


horarioHoras = float(input("Digite as horas: "))
horarioMinutos = float(input("Digite os minutos: "))
horarioSegundos = float(input("Digite os segundos: "))
minutos = horarioHoras * 60 + horarioMinutos + (horarioSegundos/60)
segundos = horarioHoras * 3600 + horarioMinutos * 60 + horarioSegundos
print("O total de minutos é: " + str(minutos) + " minutos.")
print("O total de segundos é: " + str(segundos) + " segundos.")

alturaCilindro = float(input("Digite a altura do cilíndro: "))
raioCilindro = float(input("Digite o raio do cilíndro "))
areaBase = (3.14 * (raioCilindro * raioCilindro))
areaLado = 2 * 3.14 * raioCilindro * alturaCilindro
areaTotal =  areaBase + areaLado
lataCapacidade = 15
quantidadeLatas = areaTotal/15
precoLatas = quantidadeLatas * 50
print("A quantidade de latas é de " + str(round(quantidadeLatas)))
print("Você pagará " + str(round(precoLatas)))