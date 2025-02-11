import math

while True:
    print("\n Choose the math operation. \n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to a power\n6 - Square root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent \n")

    oper = input("\n Your option from the menu: ")
# Addition
    if oper == "0":
        val1 = float(input("\n First value: "))
        val2 = float(input("\n Second value: "))

        print("\n The result of addition is: " + str(val1 + val2) + "\n")
        back = input("\n Go back to the main menu?  (y/n) ")
# Going back to the main menu or exiting program
        if back == "y":
            continue
        else:
            break
# Subtraction
    elif oper == "1":
        val1 = float(input("\n First value: "))
        val2 = float(input("\n Second value: "))

        print("\n The result of subtraction is: " + str(val1 - val2) + "\n")
        back = input("\n Go back to the main menu?  (y/n) ")
# Going back to the main menu or exiting program
        if back == "y":
            continue
        else:
            break
# Multiplication
    elif oper == "2":
        val1 = float(input("\n First value: "))
        val2 = float(input("\n Second value: "))

        print("\n The result of multiplication is: " + str(val1 * val2) + "\n")
        back = input("\n Go back to the main menu?  (y/n) ")
# Going back to the main menu or exiting program
        if back == "y":
            continue
        else:
            break
# Division
    elif oper == "3":
        val1 = float(input("\n First value: "))
        val2 = float(input("\n Second value: "))

        print("\n The result of division is: " + str(val1 / val2) + "\n")
        back = input("\n Go back to the main menu?  (y/n) ")
# Going back to the main menu or exiting program
        if back == "y":
            continue
        else:
            break
# Modulo
    elif oper == "4":
        val1 = float(input("\n First value: "))
        val2 = float(input("\n Second value: "))

        print("\n The result of modulo is: " + str(val1 % val2) + "\n")
        back = input("\n Go back to the main menu?  (y/n) ")
# Going back to the main menu or exiting program
        if back == "y":
            continue
        else:
            break
# Rising to a power
    elif oper == "5":
        val1 = float(input("\n First value: "))
        val2 = float(input("\n Second value: "))

        print("\n The result of raising to a power is: " + str(math.pow(val1, val2)) + "\n")
        back = input("\n Go back to the main menu?  (y/n) ")
# Going back to the main menu or exiting program
        if back == "y":
            continue
        else:
            break
# Square root
    elif oper == "6":
        val1 = float(input("\n Enter value for extracting the square root: "))

        print("\n The result of square root is: " + str(math.sqrt(val1)) + "\n")
        back = input("\n Go back to the main menu?  (y/n) ")
# Going back to the main menu or exiting program
        if back == "y":
            continue

        else:
            break
# Logarithm
    elif oper == "7":
        val1 = float(input("\n Enter value for logarithm: "))

        print("\n The result of logarithm is: " + str(math.log(val1, 2)) + "\n")
        back = input("\n Go back to the main menu?  (y/n) ")
# Going back to the main menu or exiting program
        if back == "y":
            continue

        else:
            break
# Sine
    elif oper == "8":
        val1 = float(input("\n Enter value in degrees for calculate sine: "))

        print("\n The result of sines is: " + str(math.sin(math.radians(val1))) + "\n")
        back = input("\n Go back to the main menu?  (y/n) ")
# Going back to the main menu or exiting program
        if back == "y":
            continue

        else:
            break
# Cosine
    elif oper == "9":
        val1 = float(input("\n Enter value in degrees for calculate cosine: "))

        print("\n The result of cosines is: " + str(math.cos(math.radians(val1))) + "\n")
        back = input("\n Go back to the main menu?  (y/n) ")
# Going back to the main menu or exiting program
        if back == "y":
            continue

        else:
            break
# Tangent
    elif oper == "10":
        val1 = float(input("\n Enter value in degrees for calculate tangent: "))

        print("\n The result of tangent is: " + str(math.tan(math.radians(val1))) + "\n")
        back = input("\n Go back to the main menu?  (y/n) ")
# Going back to the main menu or exiting program
        if back == "y":
            continue

        else:
            break