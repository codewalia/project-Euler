#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

a = 600851475143
list1 = []
list2= []


for i in xrange(1, a):
    if(a%i==0 ):
        list1.append(i)

flag = False
for i in range(1, len(list1)): #list[1] =5
    for j in range (3, list1[i]):
        if(list1[i]%j==0):
            #list2.insert(i, list1[i])
            flag = True
            #break
    if flag == False:
            list2.insert(i, list1[i])

print(list1)
print(list2)
print(list2[-1])
