
#Worldbuilding number converter
decimal = int(input('input decimal'))
constfactor =1
constfactor2=11
constfactor3=111
octal = oct(decimal) #convert base 10 to base 8 (octal)
octalval=int((octal[2:])) # remove 1st 2 characters (not needed)

if (octalval>=100):  #if greater than 100, add 111
    octaladdedval= constfactor3 + octalval
    print(octaladdedval)
else:
    if (decimal<10):  #if greater than 10, add 11, less than 10, add 1
       octaladdedval= constfactor + octalval
    else: 
       octaladdedval = constfactor2 + octalval
       print(octaladdedval)
