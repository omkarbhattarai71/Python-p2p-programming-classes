# Write a Python program to check whether an element exists within a tuple


tup=('hello','world','we','love','each','other',4,2,9,7)

for i in tup:
    if 'we' in tup:
        print(True)
        break
    else:
        print(False)
        break
        
for i in tup:        
    if 'how' in tup:
        print(True)
        break
    else:
        print(False)
        break
        
        
        
Output:
  True 
  False
