#Use List functions del(), clear(), list(), reverse(), sort(), sort(reverse=True), id(), count(), pop()
list2 = [50, 25.50, 'prashant']  
del list2[2]  
print(list2)
list2.clear()  
print(list2)  
#
name = "prashant"  
print(name)   
myname = list(name)  
print(myname)  
#
mylist = [40, 30, 20, 10]  
mylist.reverse()  
print(mylist)
#
mylist = [44, 22, 77, 0, 9, 88]  
mylist.sort()  
print(mylist)
#
mylist.sort(reverse=True)  
print(mylist) 
#
mylist = [42, 22, 77, 0, 9, 88]  
newlist = mylist  
print(id(mylist))  # Output: same id  
print(id(newlist))
#
#WAP to print the count even and odd numbers
even=0
odd=0
for i in range(1,11):
    if i%2 == 0:
        even += 1
    else:
         odd += 1
print("Even =",even)
print("Odd =",odd)
