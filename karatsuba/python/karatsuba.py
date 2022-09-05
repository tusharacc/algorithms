import math
import sys

#numbers are passed as string
def karatsuba(num1,num2):
    if len(num1) == 1 and len(num2) == 1:
        return int(num1)*int(num2)
    else:
        len_num1 = len(num1)
        len_num2 = len(num2)
        max_length = 0

        #logic to make both number of same length
        if len_num1 > len_num2:
            num2 = "0"*(len_num1 - len_num2) + num2
            max_length = len_num1
        elif len_num2 > len_num1:
            num1 = "0"*(len_num2 - len_num1) + num1
            max_length = len_num2
        else:
            max_length = len(num1)
        #make numbers of even length
        if max_length % 2 != 0:
            num2 = "0" + num2
            num1 = "0" + num1
            max_length += 1

        a = num1[0: max_length//2]
        b = num1[max_length//2:]
        c = num2[0:max_length//2]
        d = num2[max_length//2:]

        step_1 = karatsuba(a,c)
        step_2 = karatsuba(b,d)
        step_3 = karatsuba(str(int(a)+int(b)), str(int(c)+int(d)))
        step_4 = step_3 - step_1 - step_2
        step_5 = step_1*math.pow(10,max_length) + step_4*math.pow(10,(max_length/2)) + step_2

        return step_5

if __name__ == '__main__':
    number1 = sys.argv[1]
    number2 = sys.argv[2]

    print (str(karatsuba(num1=number1, num2=number2)))