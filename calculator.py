import math

print("CALCULATOR\n")
print("MENU")
print("Add")
print("Subtract")
print("Multiply")
print("Divide")
print("Power")
print("SquareRoot")
print("Factorial\n")


def check(num):
   if num.isdigit():
    num = list(map(int, input("Please enter your numbers again: ").split()))
   # for i in num:
         #print(i, end=" ")
   # print()  
    return num
   else:
    print("Enter numbers only")  
    return False
   
while True:
     num = input("Enter a number: ")
     result=check(num)
     if result:
          num=result
          break
   
#print("\n")
#num=check(num)
print("Numbers entered:",num)
#print("\n")
op=input("Enter a operation: ")

def add(num):
    sum=0
    for i in num:
        sum=sum+i
    print("Result = ",sum)

def subtract(num):
    result=num[0]
    for i in num[1:]:
        result-=i
    print("Result = ",result)

def multiply(num):
    answer=1
    for i in num:
     answer*=i
    print("Result = ",answer)

def divide(num):
    if(len(num)==2):
        try:
          if num[0] == 0 or num[1] == 0:
           raise ValueError("The first or second numbers cannot be zero.")
        except ValueError as y:
         print("Error:", y)
        else:
         x = num[0] / num[1]
         print("Result:", x)
    else:
     print("Invalid input!Enter two numbers.")

def power(j):
     if(len(j) == 2):
       x=math.pow(j[0],j[1])
       print("Result = ",x)
     else:
       print("Enter only two numbers")

def squarert(j):
     if(len(j) == 1):
       y=math.sqrt(j[0])
       print("Result = ",y)
     else:
       print("Invalid input! Please enter one number")

def fact(j):
     if(len(j) == 1):
       z=math.factorial(j[0])
       print("Result = ",z)
     else:
       print("Invalid input! Please enter one number")


match op:
    case "Add" | "add":
        add(num)
    case "Subtract"| "subtract":
         subtract(num)
    case "Multiply" | "multiply":
         multiply(num)
    case "Divide" | "divide":
         divide(num)
    case "Power" | "power":
         j=tuple(num)
         power(j) 
    case "SquareRoot" | "squareroot":
         j=tuple(num)
         squarert(j) 
    case "Factorial" | "factorial":
         j=tuple(num)
         fact(j) 
        

    case _:
        print("Invalid operation!Please select any operation from the given MENU")



# Created by Simrannsv
# GitHub: https://github.com/your-simrannsv
# Licensed under the MIT License
