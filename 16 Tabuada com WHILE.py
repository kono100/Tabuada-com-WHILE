


n = int(input('Você quer ver a tabuada de qual número? '))
resp = ''
while True:
    for c in range(1,11):
        print(f'{n} x {c:2} = {n * c}')
    resp = str(input('\nQuer ver a tabuada de outro valor? [S / N]: ')).strip().upper()
    if resp in 'Ss':
        n = int(input('Você quer ver a tabuada de qual número? '))
    else:
        break
print('\n\tFIM!\n')