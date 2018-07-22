'''
6. Determine the result of the following, and indicate with a check
mark yes or an no if they are legitimate or not:

a) 1.2 + 4                              5.2
b) '1.2' + '4'                          1.24
c) 'abc' + 'de'                         abcde
d) 1.2 * 3                              3.6
e) '1.2' * 3                            1.21.21.2
f) '1.2' + 3                            error                         
g) 4/5                                  0.8
h) 4//5                                 0
i) 7/4                                  1.75..
j) 7//4                                 1
k) 7 % 4                                0.75


7. Determine if the following are valid Python identifiers or not:

a) sam YES / no
b) soft-ware yes / NO            
c) _sam YES / no
d) 5_sam yes / NO                  
e) soft_ware YES / no
f) Sam YES / no               
g) soft\ware yes / NO
h) soft/ware yes / NO          



8. numOfPens = 5

print("I got me", numOfPens, "pens to write with")
    Display: I got me 5 pens to write with

print("He got", numOfPens+2, "pens in de pocket")
    Display: He got 7 pens in de pocket


9. x, y, z = 5, 6, 7
print("x =", x , ", y =", z , ", z =", y)
    Display: x = 5 y = 7 z = 6

10. print("abc\n\tdef\n\t" "\tghi\n\t\tSammee! ")
    Display: abc
                 def
                         ghi
                                 Sammee!

                                


11. x, y, z = 5, 6, 2
x = 5
y = 6
z = 2

Apply parentheses appropriately to get the desired answer t: 

a) t = (x + 7) * (y / z) + 4        t = 40                          
b) t = (x + 7) * y / (z + 4)        t = 12                       
c) t = x + (7 * y) / (z + 4)        t = 30                        
c) t = (x + 7) * ((y / z) + 4)      t = 84



12. s1, s2, s3 = 'q', 'we', 'rty'

Determine the result from the following:

a) 'ab' + 'zyx' =  'abzyx'
b) 'fg' * 3 = 'fgfgfg'
c) s1 * 5 = 'qqqqq'
d) 'fg' * 2 + s3 = 'fgfgrty'
e) s2 * 3 + s2 * 2 = 'wewewewewe'
f) s1 + s2 + s3 =  'qwerty'


13. Determine the output displayed for each of the following:
a) print( ‘1’ , ‘2’ , ‘3’ , ‘4’ ) Displayed: 1 2 3 4
b) print( ‘1’ + ‘2’ + ‘3’ + ‘4’ ) Displayed: 1234
c) print( ‘1’ , ‘2’ + ‘3’ , ‘4’ ) Displayed: 1 23 4
d) print( ‘1’ + ‘2’ , ‘3’ + ‘4’ ) Displayed: 12 34

14. x , y , z = 2 , 4 , “Hi”

For each of the following, identify IF Python will complain, and what about:

a) pint(“x =“, x)                                  print statement is spelt wrong
b) print(“x = “, y)                                'x = 4'
c) print(“y =“ y)                                  error ! b/c print statement connects a string with a integer without a comma
d) print(“ (x+3)*2) =“, (x+3)*2)                   " (x+3)*2 = 10"
e) print(“x = “, Y)                                error ! no variable called capital Y
f) print(“y =“ * y)                                "y =y =y =y ="
g) print(“y =“ + y)                                error ! you cannot added an integer to a string without converting it first
h) print(“y =“ + str(y))                           "y = 4"



15. dist = input(‘Enter distance in meters: ‘)                                              # Ex. user enters 8
    nStdts = int(input(‘Enter how many students: ‘))                                        # Ex. user enters 4
    
Determine the output displayed for each of the following, or if an error is
reported by Python:

a) print( nStdts + dist)
    Displayed: error nStdts is an integer and dist is a string you cannot added them

b) print( dist + nStdts )
    Displayed: cannot add an integer to a string

c) print( nStdts * dist)
    Displayed: "8888" or an error!

d) print(nStdts * int(dist))
    Displayed: 32

e) print(str(nStdts) * int(dist))
    Displayed: '44444444'

f) print(nStdts + int(dist))
    Displayed: 12

g) print(str(nStdts) + int(dist))
    Displayed: error cannot add a string to an integer and visa vera

h) print(nStdts / int(dist))
    Displayed: 1/2

i) print( int(dist) / nStdts )
    Displayed:  2





17. Write a program to produce an interactive session as exemplified below:

Greeetings!
What’s your name: Jill
G’day, Jill ! How tall are you, in cm.: 172
That makes you 67.7” tall = 5 ft 7.7 inches



'''

#17 program



print("Howdy, Stranger! How are you doing?\n")

name = input("What's your name, Stranger? \n")

print("G'day",
      name,"!",
      end = " ")

height = input("How tall are you, in cm: \n")
heightin = float(height)* 0.393701
heightft = heightin//12
heightrm = heightin - (12 * heightft)

print("That makes you",
      str(round(heightin,2)) + "\" tall =",
      str(int(heightft)) + " ft",
      str(round(heightrm, 2)) + " inches")