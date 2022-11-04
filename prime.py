num = int(input('Enter Number: '))
import math
prime = True
x = int(math.sqrt(num))
while x>1:
    if num%x ==0:
        print('The number', num, 'is NOT prime')
        prime = False 
        break
    else:
        x -= 1
        if prime:
            print('The number', num, 'is prime')
        else:
            print('The number', num, 'is NOT prime')
            
        
