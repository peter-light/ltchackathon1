#define a function for finding
#reverse of first and second number n1 and n2
def reverseNum1(n1) :
    rev1 = 0
    while (n1):
       dig = n1%10
       rev1 = rev1 *10 + dig
       n1=n1//10
    return rev1
def reverseNum2(n2) :
    rev2 = 0
    while (n2):
       dig = n2%10
       rev2 = rev2 *10 + dig
       n2=n2//10
    return rev2
#take string inputs from user
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
#assign the addition of the reversed
#numbers to a variable n3
n3 = reverseNum1(n1)+ reverseNum2(n2)
# define a function for the value
#gotten after adding the reversed n1 and reversed n2 which is n3
#and then reverses it(n3)...
def reverseNum3(n3) :
    rev3 = 0
    while (n3):
       dig = n3%10
       rev3 = rev3 *10 + dig
       n3=n3//10
    return rev3
print("Sum of reversed numbers is:",reverseNum3(n3))





