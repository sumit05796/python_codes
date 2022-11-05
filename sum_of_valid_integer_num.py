number_list = input('Enter a list of numbers separated by spaces: ')
num = number_list.split()
sum = 0
for i in num:
    try:
        int_num = int(i)
        sum =   sum + int_num
    except ValueError:
        print('entered no. could not be converted to integer', i)
print('sum of valid integer no.s : ',  sum)        
        
