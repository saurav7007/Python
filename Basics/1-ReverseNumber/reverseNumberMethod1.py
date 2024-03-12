### First Method to Reverse the input integer ###

#### Taking user input ####
inputNumber = int(input('Enter the number you want to reverse: '))

#### Declearing a variable for reversed number ####
reverseNumber = 0

#### Running a loop to reverse the input number ####
while inputNumber != 0:                               ## running a while loop untill input number becomes zero
  remainder = inputNumber % 10                        ## storing the value of remainder in a variable
  reverseNumber = reverseNumber * 10 + remainder      ## multiplying reverser number value with 10. This will increase the value of a number by 10th place. 
                                                      ## Example: 1 * 10 = 10, 10 * 10 = 100, 100 * 10 = 1000, and so on.
  inputNumber = inputNumber // 10                     ## Taking out the quotient from input number 

print('Your reverse number is :',reverseNumber)       ## Print the reversed number
