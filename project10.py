# Write a Python program to remove duplicates from a list


list1=[1,2,5,3,1,2,1,1,1,4,3,4,5,7,6,7,5,9]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
        
print(list2)
