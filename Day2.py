'''Day 2: Find the Largest Digit in a Number
'''



def largest_digit_number(number):

    largest=0
    while number>0:
        rem=number%10
        number=number//10
        if rem>largest:
            largest=rem
    # print(largest)
    return largest

num=int(input("enter the number"))
x=largest_digit_number(num)
print(x)
        
        

