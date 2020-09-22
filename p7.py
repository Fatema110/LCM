
"""
FIND THE LCM OF TWO NUMBERS
"""

a=int(input(" enter the first number :"))
b=int(input(" enter the second number:"))
if(a>b):
    min1=a
else:
    min1=b
while(1):
    if(min1%a==0 and min1%b==0):
        print("lcm is:",min1)
        break
    min1+=min1
OUTPUT-
enter the first number :32
enter the second number:67
lcm is: 2144
