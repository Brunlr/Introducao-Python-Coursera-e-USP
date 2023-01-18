print ('Exercicio 3'.center(30))
num = int(input('Digite um numero para saber se ele é divisivel por 3: '))
if num%5==0 and num%3==0:
    print ('FizzBuzz')
else:
    print (num)