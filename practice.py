intro = input("Write Something About Your Self: ")
chrcount = 0
wordcount = 1
for i in intro : 
     chrcount = chrcount + 1
     if(i==" "):
         wordcount = wordcount + 1

print("No Of Words in Your indtroduction")
print(wordcount)
print(chrcount)