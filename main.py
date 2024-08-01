import math
import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa as crypto_rsa

def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

def obterPrimos(n):
    primos = []
    for i in range(2, n + 1):
        eh_primo = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(i)
    return primos

def fatorar(n):
    primos = obterPrimos(int(math.sqrt(n)))
    for p in primos:
        if n % p == 0:
            q = n // p
            return p, q
    return None, None

def encontrarFatoresPrimos(n):
    fatores = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            fatores.append(i)
            n //= i
    if n > 1:
        fatores.append(n)
    return fatores

def calcularChavePR(p, q, e):
    if p is None or q is None:
        return None
    
    euler = (p - 1) * (q - 1)
    
    if math.gcd(e, euler) != 1:
        raise ValueError('\nO expoente público (e) não é invertível para o dado módulo (euler). Escolha outro valor para e.')

    d = pow(e, -1, euler)
    return d

try:
    print('ATENÇÃO - O comprimento do módulo não deve ultrapassar 2^16 (65.536).\n')
    n = int(input('Digite o valor do módulo (n - Deve ser resultado do produto de dois números primos diferentes): '))
    e = int(input('Digite o valor do expoente público (e - Deve ser um número primo): '))

    fatores = encontrarFatoresPrimos(n)
    if len(fatores) != 2:
        print('\nPor favor, insira valores válidos.')
        exit()

except ValueError as ve:
    print(f'\nPor favor, insira valores válidos. {ve}')

else:
    if n > 2**16:
        print('O comprimento do módulo não deve ultrapassar 2^16 (65.536).')
    else:
        p, q = fatorar(n)
        if p is None or q is None:
            print('Não foi possível fatorar o módulo.')
        else:
            d = calcularChavePR(p, q, e)
            if d is not None:
                print(f'\nMódulo (n): {n}')
                print(f'Expoente Público (e): {e}')
                print(f'Expoente Privado (d): {d}')
                print(f'Números primos (p e q): {p}, {q}')
                print(f'Valores da Chave Pública (e, n): {e}, {n}')
                print(f'Valores da Chave Privada (d, n): {d}, {n}')
            else:
                print('Não foi possível calcular os valores para a chave privada.')