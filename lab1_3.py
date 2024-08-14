n = 0
while n <= 0 or n >= 9:
    try:
        n = int(input("Введіть висоту пірамідки - "))
        if n <= 0 or n >= 9:
            print("Висота не підлягає діапазону (0<n<9)")
    except ValueError:
        print("Невірний тип розміру пірамідки")


for i in range(n-1, -1, -1):
    print(' ' * (i*2), end='')
    for j in range(i+1, n+1):
        print(j, end=' ')
    print()