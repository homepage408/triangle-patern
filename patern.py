n = int(input('Masukan angka : '))

print('Patern ke-1')
for i in range(0, n):
    for j in range(0, i+1):
        print('*', end='')
    print()


print('Patern ke-2')
for i in range(0, n):
    for j in range(n, i, -1):
        print('*', end='')
    print()

print('Patern ke-3')
for i in range(0, n):
    for j in range(0, i):
        print(' ', end='')
    for k in range(n, i, -1):
        print('*', end='')
    print()

print('Patern ke-4')
for i in range(0, n):
    for j in range(n, i, -1):
        print(' ', end='')
    for k in range(0, i+1):
        print('*', end='')
    print()
