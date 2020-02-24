#!/usr/bin/env python3

# Created by C0rqScr3W (https://github.com/C0rqScr3W)
# Improvements by inc0gnit0 (https://github.com/iinc0gnit0)

# Dependencies
from webbrowser import open

# Colors
red = "\033[91;1m"
reset = "\033[0m"
green = "\033[92;1m"
cyan = "\033[96;1m"
yellow = "\033[93;1m"
magenta = "\033[95;1m"
blue = "\033[94;1m"
white = "\033[97;1m"
blink = "\033[5m"

# Options
def add(x, y):
    return x + y

def subtract(x,y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

def modulo(x, y):
    return x % y

def ex(x, y):
    return x ** y

def floord(x, y):
    return x // y

def main():
    # Print Options
    print(green + "select a choice:\n")
    print(red + "0\n")
    print(cyan + "1.add\n")
    print(yellow + "2.subtract\n")
    print(magenta + "3.multiply\n")
    print(blue + "4.divide\n")
    print(red + "5.Remainder\n")
    print(green + "6.Exponent\n")
    print(cyan + "7.Floor Division\n")
    print(yellow + "60.youtube\n")
    print(magenta + "70.netflix\n")
    print(blue + "80.hulu\n")
    print(red + "90.pypi\n")
    print(green + "100.pyhelp\n")
    print(cyan + "31.pi\n")
    print(yellow + "143.htb\n")

    # Input
    choice = input(magenta + "\nChoose a Number: 1-2-3-4-5-6-7: ")
    num1 = input(blue + "\nput a number: ")
    num2 = input(red + "\nput another number: ")

    print("\n\n")

    # Pi
    if choice == "31":
        print(cyan + " pi == 3.1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679 ")

    elif choice == "143":
        open("hackthebox.eu")

    elif choice == "60":
        open("youtube.com")

    elif choice == "70":
        open("netflix.com")

    elif choice == "80":
        open("hulu.com")

    elif choice == "90":
        open("pypi.org")

    elif choice == "100":
        open("docs.python.com")

    elif choice == "0":
        print(red + " I Hate Math!! ")

    elif choice == "1":
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == "2":
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == "3":
        print(num1, "*", num2, "=", mult(num1, num2))

    elif choice == "4":
        print(num1, "/", num2, "=", div(num1, num2))

    elif choice == "5":
        print(num1, "%", num2, "=", modulo(num1, num2))

    elif choice == "6":
        print(num1, "**", num2, "=", ex(num1, num2))

    elif choice == "7":
        print(num1, "//", num2, "=", floord(num1, num2))

    else:
        print(red + "Invalid Input" + reset)

# Error Handling
try:
    if __name__ == '__main__':
        main()

except KeyboardInterrupt:
    print(red + '\n\nControl + C Detected... Exiting' + reset)
    exit(1)

except:
    print(red + '\n\nAn Error Occured... Exiting' + reset)
    exit(1)