from collections import Counter
s=input("enter a string ") 
# data structure like dictionary , list, set, tuple
# dictionary : contain key and value {1: 'habiba', 2:'malak'} , so he search with the value if it matches the dictionary values will increment the key 
# set : store unique values ,but doesnot have counter. Couldnot do an external counter as it may be large number of diffrent characters
# tupple or string : due to immutability 
letter_count=Counter(s)
print(letter_count) #return dictionary with key and value
result="" # result=0 it will be integer 
for char,count in letter_count.items():
    result += f"{char}{count}"
print(result)
 
