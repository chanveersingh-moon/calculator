# this code is written by chanveersingh follow on github for more

wl ="welcome to calculator calculate the value you want"
opp = ("1.addition\n"
       "2.subraction\n"
       "3.division\n"
       "4.multiplication\n"
       "5.float division\n"
       "6.EXIT")

y = "your result is :"
print(wl)
print(opp)

option = int(input("enter your option from above:"))
number1 = float(input("enter your first number:"))
number2 = float(input("enteryour second nuber:"))

# if else will give result with opratores of python

if option == 1:
    print(y,number1 + number2)
elif option == 2:
    print(y,number1 - number2)
elif option == 3:
    print(y,number2 / number1)
elif option == 4:
    print(y,number1*number2)
elif option == 5:
    print(y,number1//number2)
elif option == 6:
    print("bye bye have a nice day #")
    exit()
else:
    print("you value is invailed")

