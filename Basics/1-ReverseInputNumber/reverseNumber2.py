### Second Method to Reverse the input integer ###

#### Taking user input as a string ####
inputNumber = input('Enter the number you want to reverse: ')

#### Declearing a variable for reversed number as string ####
reverseNumber = ''

#### Running a loop to reverse the input number ####
for number in inputNumber:
  reverseNumber = number + reverseNumber              ## Appending each character in the start of a string

reverseNumber = int(reverseNumber)                    ## Type casting the string into number
  
print('Your reverse number is :',reverseNumber)       ## Print the reversed number
