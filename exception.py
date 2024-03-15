#!/usr/bin/python3

def safeIntegerInput(prompt):
    inputString = input(prompt)
    try:
        return int(inputString)
    except ValueError:
        print("Invalid input, please enter a number")
        return safeIntegerInput(prompt)
    
if __name__ == "__main__":
    print("Enter your age")
    x = safeIntegerInput("> ")
    print(x)