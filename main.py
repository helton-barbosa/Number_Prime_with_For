number = int(input('Entre com um número inteiro: '))
count = 0

for contador in range(1, number+1):
    if number % contador == 0:
        count += 1

if count < 3:
    print(f'{number} é um número primo')
else:
    print(f'{number} não é um número primo')
