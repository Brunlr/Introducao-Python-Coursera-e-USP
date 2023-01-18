num = input("Digite um número inteiro: ")
num = int(num)

# Inicializando a variável soma com zero
soma = 0

# Iterando sobre os dígitos do número
for digito in str(num):
    soma += int(digito)

# Imprimindo a soma dos dígitos
print(soma)