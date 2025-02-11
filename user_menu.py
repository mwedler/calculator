import math

while True:
    print("\n Choose the math operation. \n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to a power\n6 - Square root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent \n")

    oper = input("\n Your option from the"
                 " menu: ")
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

        print("\n The result of Division is: " + str(val1 / val2) + "\n")
        back = input("\n Go back to the main menu?  (y/n) ")
# Going back to the main menu or exiting program
        if back == "y":
            continue
        else:
            break