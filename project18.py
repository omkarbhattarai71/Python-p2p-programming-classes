# Python program to count number of vowels using sets in given string

string="Equation and Dialogue"

c=0

vowel=set("AEIOUaeiou")

for i in string:
    if i in vowel:
        c+=1

print("The number of vowels is: ",c)

Output:

The number of vowels is:  11
