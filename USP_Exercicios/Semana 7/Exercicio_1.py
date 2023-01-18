l = int(input('Digite a largura: '))
a = int(input('Digite a altura: '))
if l<=0 or a<=0:
    print('ERRO! Tente novamente')
else:
    for c in range (0,a):
        print ('#'*l)