 # Write a Python program to count the occurrences of each word in a given sentence

sentence="I appreciate you for seeing my code for free as my code is free for all"

c= dict()
words= sentence.split()


for word in words:
    if word in c:
        c[word]+=1
    else:
        c[word]=1
    
print("Words with occurrences is given below::")
print()
print(c)


Output:
  
Words with occurrences is given below::

{'I': 1, 'appreciate': 1, 'you': 1, 'for': 3, 'seeing': 1, 'my': 2, 'code': 2, 'free': 2, 'as': 1, 'is': 1, 'all': 1}
