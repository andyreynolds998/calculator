# description of what the system is doing
"""
Script: Simple calculator
Author: Andrew Reynolds
Year: 2021
Functionality: Basic mathematical operations
"""

# imports

# globals

# functions


def print_menu():
    print("_" * 30)
    print(" PyCalc")
    print("_" * 30)

    print("[1] - Sum")
    print("[2] - Subtract")
    print("[3] - Multiplication")
    print("[4] - Division")
    print("[q] - Quit")

    # instructions


selected_option = ""
result_checker = ""
messageMachine = ""
messageBox = ""
userMultResponse = ""
userMultInput = ""

while(selected_option != "q"):
    print_menu()
    selected_option = input("Please select an option: ")

    if(selected_option == 'q'):
        break

    num1 = float(input("Provide num 1: "))
    num2 = float(input("Provide num 2: "))
    result = 0

    if(selected_option == "1"):
        result = num1 + num2
        print(result)
    elif(selected_option == "2"):
        result = num1 - num2
        print(result)
    elif(selected_option == "3"):
        result = num1 * num2
        print(result)
    elif(selected_option == "4"):
        if(num2 == 0):
            print("you can't divide by zero.")
        else:
            print(num1 / num2)

    result_checker = input("[Enter] - Is it even?")

    if(result % 2 == 0):
        print("It's even!")
    else:
        print("It's not even :(")

    messageMachine = input("[8] - Would you like to leave a message?")
    messageBox = input("What is your message?")
    userMultInput = float(
        input("How many times do you want to see your message?"))
    userMultResponse = 0
    message = ""
    multiplier = 1

    if(messageMachine == 8):
        message = messageBox
        userMultResponse = int(userMultInput)
        message = message * userMultResponse
        print(message)
    else:
        print("Alright then, have a nice day!")
