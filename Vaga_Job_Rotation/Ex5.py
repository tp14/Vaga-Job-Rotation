import math

if __name__ == '__main__':
    print("Digite uma string")
    str = input()
    list(str)

    aux = len(str)-1
    resultado = list()
    for i in range(len(str)):
        resultado.append(str[aux])
        aux += -1

    for i in range(len(str)):
        print(resultado[i], end="")