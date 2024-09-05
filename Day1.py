"""**Day 1: Sum of Digits in a Number**
- **Problem**: Write a program that takes an integer as input and returns the sum of its digits.
- **Sample Input**: `1234`
- **Sample Output**: `10` (1 + 2 + 3 + 4)
"""

#Method 1:

def sum_of_numbers(number):

    total=0
    while number>0:
        rem=number%10
        total=total+rem
        number=number//10
    return total


num=int(input("enter the number"))
result=sum_of_numbers(num)
print(result)



#first we will convert the number to string
#after that we will take each number from string and convert it to int and add it to total

def sum_of_number(number):

    num=str(number)
    print(type(num))
    sum=0
    for i in num:
        sum=sum+int(i)
    return sum


num=int(input("Enter the number"))
result=sum_of_number(num)
print(result)
