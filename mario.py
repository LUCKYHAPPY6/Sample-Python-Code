height = int(input('please pick a number between 1 and 8 ' ))
while not 1<= height<= 8:
    height = int(input('please pick a number between 1 and 8 '))

for i in range(1, height + 1):
    for j in range(1 , height + 1):
        if i <= height -j:
            print(' ', end='')
        else:
            print('#', end='')
    print('\n')







