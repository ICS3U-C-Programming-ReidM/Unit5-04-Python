#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: May 2025
# This program calculates the result of two numbers using the calculate(sign, first_number, second_number) function


def calculate(sign, first_number, second_number):
    # This function performs the selected operation
    if sign == "+":
        return first_number + second_number
    elif sign == "-":
        return first_number - second_number
    elif sign == "*":
        return first_number * second_number
    elif sign == "/":
        if second_number == 0:
            return "Error: Division by zero"
        return first_number / second_number
    elif sign == "%":
        if second_number == 0:
            return "Error: Modulo by zero"
        return first_number % second_number
    else:
        return "Invalid operator"


def main():
    # This function gets user input and calls the calculate function
    sign = input("Enter the operator (+, -, *, /, %): ")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    result = calculate(sign, first_number, second_number)
    print(f"The result of {first_number} {sign} {second_number} is: {result}")


if __name__ == "__main__":
    main()
