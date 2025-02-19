x=int(input()) #to get input
lst=list() #creating a list
for i in range(x): #using for loop for appending the lst(list)
    if i == 0:
        lst.append(0)
    elif i == 1:
        lst.append(1)
    else:
        sum=int(lst[i-2])+int(lst[i-1])
        lst.append(sum)
print(lst) #Printing the Fibonacci sequence
