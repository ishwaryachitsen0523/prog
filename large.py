num1 = 10
num2 = 14
num3 = 12
num4 = 16
num5 = 17
num6 = 11
num7 = 14
num8 = 13
num9 = 19
num10 = 20
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter third number: "))
num5 = float(input("Enter third number: "))
num6 = float(input("Enter third number: "))
num7 = float(input("Enter third number: "))
num8 = float(input("Enter third number: "))
num9 = float(input("Enter third number: "))
num10 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3) and (num1 >= num4) and (num1 >= num5) and (num1 >= num6) and (num1 >= num7) and (num1 >= num8) and (num1 >= num9) and (num1 >= num10):
   largest = num1
elif (num2 >= num1) and (num2 >= num3) and (num2 >= num4) and (num2 >= num5) and (num2 >= num6) and (num2 >= num7) and (num2 >= num8) and (num2 >= num9) and (num2 >= num10):
   largest = num2
elif (num3 >= num1) and (num3 >= num2) and (num3 >= num4) and (num3 >= num5) and (num3 >= num6) and (num3 >= num7) and (num3 >= num8) and (num3 >= num9) and (num3 >= num10):
   largest = num3
   #follws the above elif till 9
else:
   largest = num10

print("The largest number between"numbers are"is",largest)
