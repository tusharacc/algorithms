import sys

def insertion_sort(items):
    for i in range(1,len(items)):
        j = i
        while True:
            if items[j] < items[j-1]:
                items[j],items[j-1] = items[j-1], items[j]
                j = j - 1
                if j < 1:
                    break
            else:
                break

if __name__ == '__main__':
    number_of_items = int(sys.argv[1])
    items  = []
    for i in range(number_of_items):
        items.append(int(sys.argv[i+2]))
    
    print (items)
    insertion_sort(items=items)
    print (items)