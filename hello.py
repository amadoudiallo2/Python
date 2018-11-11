"""
Program that prints a number's power
twoo arguments:
1- num - the number.
2- xpo - the xpo.
"""
def powInt(num,xpo):
    if(xpo==1):
        return(num)
    if(xpo!=1):
        return(num*powInt(num,xpo-1))
num=int(input("Please enter a number: "))
xpo=int(input("What  is the value of the exponent? "))
print("The value of the result is:",powInt(num,xpo))
