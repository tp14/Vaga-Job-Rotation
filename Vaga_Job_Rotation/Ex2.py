import math

if __name__ == '__main__':
    print("Digite um número")
    num = int(input())
    v1 = 0
    v2 = 1
    v3 = 0
    
    while(num > v3):
        v3 = v1 + v2 
        v1 = v2 
        v2 = v3
        print('v3:', v3)

    if(num == v3 or num == 0 or num == 1):
        print("O número pertence a sequencia")
    else: 
        print("O número não pertence a sequencia") 
    

