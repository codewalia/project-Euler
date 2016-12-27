# find the sum of multiples of 3 and 5 below 1000
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23

#sum = 0
#i = 0

def calculate_sum():
    sum = 0
    for i in range(1,1000):
        if (i%3==0 or i%5==0):
            sum += i
        i+=1
    return sum

print(calculate_sum())
