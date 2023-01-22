import math
import random

MAX_LENGTH = 10

array = []

i = 0

while i < MAX_LENGTH:
    random_num = random.randint(1,100)
    if array.count(random_num) == 0:
        array.append(random_num)
        i += 1

array = sorted(array)



def get_diff_and_index(array):
    lower_index = 0
    upper_index = 0
    while True:
        lower_index = random.randint(0,MAX_LENGTH-1)
        upper_index = random.randint(0,MAX_LENGTH-1)

        if upper_index > lower_index:
            break
        elif upper_index < lower_index:
            lower_index,upper_index = upper_index,lower_index
            break

    print ("upper & lower index",lower_index,upper_index)
    #print (array)
    d = array[upper_index] - array[lower_index]

    return d, lower_index, upper_index

def get_the_index(array,d):
    print ("Distance",d)
    j = 1
    counter = 1
    found = False
    end_loop = False
    for i in range(0,MAX_LENGTH-1):

        counter += 1
        if i == j:
            j += 1
        while True:
            counter += 1
            if array[j] - array[i] == d:
                found = True
                break
            elif array[j] - array[i] < d:
                j += 1
                if j > MAX_LENGTH - 1:
                    end_loop = True
                    break
            elif array[j] - array[i] > d:
                break
        if end_loop:
            break
        if found:
            break
    
    print ("Counter", counter)
    if found:
        print ("Found",i,j)
    else:
        print ("not Found")

def get_array(number_of_items):
    array = []
    a = 0
    b = a + 10
    for i in range(0,number_of_items):
        array.append(random.randint(a,b))
        a = b+1
        b = a + 10
    return array

array = get_array(MAX_LENGTH)
d,l,h = get_diff_and_index(array=array)
get_the_index(array=array,d=d)