import math

def extended_euclid(a,b):
    if b == 0:
        return (a,1,0)
    else:
        d_1,x_1,y_1 = extended_euclid(b, a%b)
        print (d_1, x_1, y_1)
        d,x,y = d_1,y_1,x_1 - math.floor(a/b)*y_1
        return (d,x,y)

if __name__ == '__main__':
    print (extended_euclid(24,18))