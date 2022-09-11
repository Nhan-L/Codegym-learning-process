a = input ('Nhập số a: ')
int_a = int(a)
b = input ('Nhập số b: ')
int_b = int(b)
if int(a[-1]) < int(a[0]) or int(b[-1]) < int(b[0]):
    a = input ('Nhập lại số a (số cuối lớn hơn số đầu): ')
    int_a = int(a)
    b = input ('Nhập lại số b (số cuối lớn hơn số đầu): ')
    int_b = int(b)
else:
    for x in range(int(a[0]), int(a[-1]) + 1):
        if x % 3 == 0 and x % 5 == 0:
            print("Fizz buzz")
        elif x % 3 == 0:
            print('Fizz')
        elif x % 5 == 0:
            print('Buzz')
        else:
            print('x','=',str(x))
    for y in range(int(b[0]), int(b[-1]) + 1):
        if y % 3 == 0 and x % 5 == 0:
            print("Fizz buzz")
        elif y % 3 == 0:
            print('Fizz')
        elif y % 5 == 0:
            print('Buzz')
        else:
            print('y','=',str(y))        