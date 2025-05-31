# 1 positivo_nulo_negativo
def positivo_nulo_negativo(numero):
    if numero > 0:
        print("Valor Positivo")
    elif numero == 0:
        print("Valor Nulo")
    else:
        print("Valor Negativo")

if __name__ == '__main__':
    numero = float(input("Digite um número real: "))
    positivo_nulo_negativo(numero)

# 2 valor_absoluto (sem abs())
def valor_absoluto(numero):
    if numero < 0:
        return -1 * numero
    else:
        return numero

if __name__ == '__main__':
    numero = float(input("Digite um número: "))
    absoluto = valor_absoluto(numero)
    print("O valor absoluto é:", absoluto)

# 3 Calculadora com quatro operações
def somar(a, b):
    resultado = a + b
    print("Resultado da soma:", resultado)

def subtrair(a, b):
    resultado = a - b
    print("Resultado da subtração:", resultado)

def multiplicar(a, b):
    resultado = a * b
    print("Resultado da multiplicação:", resultado)

def dividir(a, b):
    if b != 0:
        resultado = a / b
        print("Resultado da divisão:", resultado)
    else:
        print("Erro: divisão por zero não é permitida.")

if __name__ == '__main__':
    operador = input("Digite a operação (+, -, x, /): ")
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if operador == "+":
        somar(a, b)
    elif operador == "-":
        subtrair(a, b)
    elif operador.lower() == "x":
        multiplicar(a, b)
    elif operador == "/":
        dividir(a, b)
    else:
        print("Operador inválido.")

# 4 fatorial
def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

if __name__ == '__main__':
    numero = int(input("Digite um número inteiro para calcular o fatorial: "))
    if numero < 0:
        print("Fatorial não definido para números negativos.")
    else:
        resultado = fatorial(numero)
        print(f"O fatorial de {numero} é {resultado}")
