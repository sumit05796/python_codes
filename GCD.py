number = input('Enter two no.s separated by space: ')
num1 = int(number.split()[0])
num2 = int(number.split()[1])
while num2 !=0:
    k = num2
    num2 = num1%num2
    num1 = k
11print('number1- ', num1, 'number2- ', num2)    