import random

def get_array(number_of_items):
    array = []
    a = 0
    b = a + 10
    for i in range(0,number_of_items):
        array.append(random.randint(a,b))
        a = b+1
        b = a + 10
    return (array,a-1)

def get_index_for_d(array,d):
    i = 0
    j = 1
    prev_i = 0
    prev_d = 0
    found = False
    counter = 1
    while True:
        counter += 1
        diff = array[j] - array[i]
        if prev_d + diff == d:
            found = True
            break
        elif prev_d + diff < d:
            prev_d += diff
            if prev_i == 0:
                prev_i = i
        elif prev_d + diff > d:
            prev_d = diff
            prev_i = i

        i += 1
        j += 1
        if j > len(array) - 1:
            break

    print ("counter",counter)

    if found:
        print ("Found", prev_i,j)
        return (prev_i,j)
    else:
        print ("Not Found")
        return (0,0)


if __name__ == '__main__':
    number_of_items = 10
    array,max = get_array(number_of_items)

    index_1 = random.randint(0,number_of_items-1)
    index_2 = random.randint(0,number_of_items-1)

    print ("index", index_1, index_2)
    d = abs(array[index_1] - array[index_2])

    print ("array",array)
    print ("difference",d)

    i,j = get_index_for_d(array,d)
