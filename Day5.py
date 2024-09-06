# '''*Day 5: Count the Frequency of Each Character in a String*
# •⁠  ⁠*Problem*: Write a program to count the frequency of each character in a given string.
# •⁠  ⁠*Sample Input*: ⁠ "programming" ⁠
# •⁠  ⁠*Sample Output*: ⁠ {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1} ⁠'''

# #learn dictionaries


# my_dict={}
# print(my_dict)

# my_dict={
#     "name":"pradeep",
#     "age":24
# }
# print(my_dict)

# # for i in my_dict:
# #     print(i) #name age (key is printed)
# #     print("-------------")
# #     print(my_dict[i]) #key values are printed

# for values in my_dict.values():
#     print(values) # values are printed




def freq_each_ele(string1):
    my_dict={}
    for i in string1:
        if i in my_dict:
            my_dict[i]+=1
        else:
            my_dict[i]=1
    return my_dict

string1=input('Enter the element : ')
k=freq_each_ele(string1)
print(k)


        





        
















