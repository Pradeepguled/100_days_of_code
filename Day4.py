'''Day 4: Check if Two Strings are Anagrams**
- **Problem**: Write a program to check if two given strings are anagrams of each other.
- **Sample Input**: `"listen"`, `"silent"`
- **Sample Output**: `True`'''



def anagrams(str1,str2):
    k='False'
    if(len(str1)==len(str2)):
        if(sorted(str1)==sorted(str2)):
            k='True'
        else:
            k='False'
    return k
    

string1=input('Enter the string1: ')
string2=input('Enter the string2: ')
callfunc=anagrams(string1,string2)
print(callfunc)

