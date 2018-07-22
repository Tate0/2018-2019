'''
ask for user's temp (F)
convert to c
generate random number between -5 and +5
predict tmr weather using random number
display results

'''

userTempF = int(input("What is the temperature today in Fahrenheit: "))
from random import randint

userTempC = int((userTempF - 32)*(5/9))

randomNum = randint(-5,5)
print('Your temperature in Celcius is:', userTempC)
print('Random number is:', randomNum)
print('Tomorrows weather is going to be',
      (randomNum + userTempC))
