number = int(input('Enter number: '))
def find_avg(n):
    sum = 0
    for number in range(1,n+1):
        sum = sum + number
        avg = float(sum/n)
    print('sum- ', sum)
    return avg
print('average of', number, 'natural no.s = ', find_avg(number))
