from time import time
start_time = time()

#A function that returns the maximum value of a python list#
def find_max(list_1):
    biggest = list_1[0]
    for i in list_1:
        if i > biggest:
            biggest = i
    return biggest
find_max([2,3,4,1,5,6])
print(find_max)      
       
end_time = time()
elapsed = end_time - start_time
print('start time is = ' ,start_time)
print('end time is = ' ,end_time)
print('elapsed time is = ' ,elapsed)