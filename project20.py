# Write a Python program to find the repeated items of a tuple


tup=('hello','people','how','are','you','we','are','with','you',1,3,1,9)


for word in tup:       
    c=tup.count(word)
    print("{}={}".format(word,c))
    
    
    
Output:
  hello=1
  people=1
  how=1
  are=2
  you=2
  we=1
  are=2
  with=1
  you=2
  1=2
  3=1
  1=2
  9=1
