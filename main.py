# the problem if we have multiple of characters are repeated
s=input("please enter a string : ")
sorted_s = sorted(s)
count=1
result=""
for i in range(1,len(s)):
    if sorted_s[i]==sorted_s[i-1]: # if the current character is same as previous one
        count+=1
    else:
        result += f"{count}{sorted_s[i-1]}"
        count=1 #Restart the count again 
result += f"{count}{sorted_a[-1]}" # -1 here means to count until the last character ,as it doeanot has any char after that so it willnot be included  
# cannot do result=any thing because string is immutable plus it will overwrite the previous result