import random
import sys

MAX_DATA = 2
#prices = list(range(100,0,-1))
prices = []
#print (prices)
counter = 0
while counter < MAX_DATA:
    prices.append(random.randint(1,100))
    counter += 1

print (prices)

buy = 0
sell = 0
temp_buy = 0
counter = 0

while counter < MAX_DATA:
    if counter == 0:
        #buy = prices[counter]
        temp_buy = prices[counter]
    else:
        if prices[counter] > temp_buy:
            if (prices[counter] - temp_buy > sell - buy):
                buy = temp_buy
                sell = prices[counter]
        else:
            temp_buy = prices[counter]
        
    counter += 1
print (counter)
print (buy,sell)