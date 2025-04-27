# This code returns the sum of the digits of the given number
sum=0
n=int(input("Enter a number:"))
original_n=n

while(n>0):
    rem=n%10
    sum=sum+rem
    n=n//10
    
print(f"The sum of the digits of number {original_n} is {sum}")