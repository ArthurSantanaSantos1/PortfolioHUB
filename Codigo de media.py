# problema 1

soma = 0
ct_1 = 0
maiores = 0
print('Digite 0 para sair:')
while True:
    valor = float(input('Digite a valor:'))
    if valor == 0:
        break
    ct_1 = ct_1 + 1
    if valor > 20:
        maiores = maiores + 1
    soma = soma + valor

md = soma / ct_1
print('numero de valores:',ct_1)
print('soma dos valores:', soma)
print('Média dos valores:', md)
print('Quantidade de valores maiores que 20',maiores)

# prpblema 2

aprovados = 0
reprovados = 0
print('digite [0] para finalizar o calculo')
while True:
    nota = float(input('Nota do aluno: '))
    if nota == 0:
        break
    if nota >= 5:
        aprovados = aprovados + 1
    if nota < 5:
        reprovados = reprovados + 1

alunos = aprovados + reprovados
print('Quantidade de alunos aprovados: ',aprovados)
print('Quantidade de alunos reprovados: ',reprovados)
print('Quantidade de alunos que fizeram a prova:', alunos)

# problema 3
impar=0
par=0
soma1 = 0
soma2= 0
print('Digite [0] para fazer o calculo dos valores.')
while True:
    numero = int(input('Digite um valor:'))
    if numero == 0:
        break
    if (numero % 2) == 0:
        soma1= numero + soma1
        par = par + 1
    soma2 = numero + soma2
    impar = impar + 1
media1 = soma1 / par
media2 = soma2 / impar

print('Média dos números pares:',media1 )
print('Média dos números impares:',media2 )
