    
# Write a Python program to calculate the length of a string.

#without function
string= "Omkar Bhattarai"
s=0
for i  in string:
    s=s+1
print("Length of string is {}".format(s))   #including space


#with function
print("Length of string is: {}".format(len(string)))



 Output:
    Length of string is 15
    Length of string is: 15
