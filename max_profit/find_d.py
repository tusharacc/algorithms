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



# # prev_random = 0
# # while i < MAX_LENGTH:
# #     random_num = random.randint(prev_random,math.pow(10,i+1))
# #     prev_random =random_num
# #     array.append(random_num)
# #     i += 1

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

print (lower_index,upper_index)
d = array[upper_index] - array[lower_index]

print (array)
print (d)
i=0
counter = 1

j = MAX_LENGTH
prev = False
prev_value = 0
mid = 0
while True:
    mid = i + (j - i) // 2
    if mid == 0 or mid == MAX_LENGTH - 1:
        break
    if array[mid] > d:
        j = mid
        prev = True
    elif array[mid] < d:
        if prev:
            j = prev_value
        else:
            i = mid


print (mid)

