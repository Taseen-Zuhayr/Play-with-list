x = [4,6,45,5,65,4547,4,3,54,732]
print("For your kind information the list is ",x)
count = 0

for i in x:
    count += i

avg = count/len(x)
print("The average is : ",avg)

x.sort()
print("The smallest number is : ",x[0])
print("The largest number is : ",x[-1])
