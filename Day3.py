'''**Day 3: Reverse a String Using a Loop**
- **Problem**: Write a program to reverse a given string using a loop.
- **Sample Input**: `"hello"`
- **Sample Output**: `"olleh"`
'''
# string1='pradeep k'
# rev=''
# for i in string1:
#     rev=i+rev
#     print(i)
# print(rev)

def reverse_a_string(sentence):
    reverse_string=''
    for i in sentence:
        reverse_string=i+reverse_string
    return reverse_string

sent=input("enter the string")
k=reverse_a_string(sent)
print(k)
    