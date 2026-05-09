
from pyscript import web, when

@when("click", "#translate-button")
def translate_english(event):

#Worldbuilding number converter
 inputval = web.page["number"]  #fix error related to no input
 if (inputval.value == ''):
    decimal = 0
 else: 
    decimal = int(inputval.value)  #input decimal into converter
 constfactor = 1  #conversion factors
 constfactor2 = 11
 constfactor3 = 111
 constfactor4 = 1111
 octal = oct(decimal) #convert base 10 to base 8 (octal)
 octalval=int((octal[2:])) # remove 1st 2 characters (not needed)
 #bypass #s 0-8
 if (decimal<=8):
 
     output_div = web.page["output"]
     output_div.innerText = decimal
 else:
 
   if (octalval>=1000):  #if greater than 1000, add 1111
     octaladdedval= constfactor4 + octalval
     output_div = web.page["output"]
     output_div.innerText = octaladdedval
   else:


    if (octalval>=100):  #if greater than 100, add 111
      octaladdedval= constfactor3 + octalval
      output_div = web.page["output"]
      output_div.innerText = octaladdedval
    else:
      if (octalval<10):  #if greater than 10, add 11, less than 10, add 1
         octaladdedval= constfactor + octalval
         output_div = web.page["output"]
         output_div.innerText = octaladdedval
      else: 
        octaladdedval = constfactor2 + octalval
        output_div = web.page["output"]
        output_div.innerText = octaladdedval
