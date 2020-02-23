import webbrowser

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

print("select a choice:")
print "0"
print "1.add"
print "2.subtract"
print "3.multiply"
print "4.divide"
print "5.Remainder"
print "6.Exponent"
print "7.Floor Division"
print "60.youtube"
print "70.netflix"
print "80.hulu"
print "90.pypi"
print "100.pyhelp"
print "31.pi"
print "143.htb"


choice = input("Choose a Number: 1-2-3-4-5-6-7: ")
num1 = int(input("\n put a number: "))
num2 = int(input("\n put another number: "))

print("\n\n")

if choice == 31:
    print " pi == 3.1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679 "

elif choice == 143:
    webbrowser.open("hackthebox.eu")

elif choice == 60:
    webbrowser.open("youtube.com")

elif choice == 70:
    webbrowser.open("netflix.com")

elif choice == 80:
    webbrowser.open("hulu.com")

elif choice == 90:
    webbrowser.open("pypi.org")

elif choice == 100:
    webbrowser.open("docs.python.com")

elif choice == 0:
    print " I Hate Math!! "

elif choice == 1:
    print num1, "+", num2, "=", add(num1, num2)

elif choice == 2:
    print num1, "-", num2, "=", subtract(num1, num2)

elif choice == 3:
    print num1, "*", num2, "=", mult(num1, num2)

elif choice == 4:
    print num1, "/", num2, "=", div(num1, num2)

elif choice == 5:
    print num1, "%", num2, "=", modulo(num1, num2)

elif choice == 6:
    print num1, "**", num2, "=", ex(num1, num2)

elif choice == 7:
    print num1, "//", num2, "=", floord(num1, num2)

else:
    print("Invalid Input")
           

           
