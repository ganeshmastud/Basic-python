def count(s, c) :  
    count = 0
    for i in range(len(s)) : 
        if (s[i] == c): 
            count +=  1
    return count
str=input("Enter the String:")
c = 'a'
print(count(str, c)) 
