def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y!=0:
      return x/y
    else:
      return "Division by zero is not possible!"
def mod(x,y):
    if y!=0:
      return x%y
    else:
      return "Can't find the reminder for Zero Division!"

ch=1
while(ch):
 a=float(input("\nEnter first operand:"))
 b=float(input("\nEnter second operand:"))
 operator=input("\nEnter desired operation(+,-,*,/,%):")
 if(operator=="+"):
    print("Result=",add(a,b))
 elif(operator=="-"):
    print("Result=",subtract(a,b))
 elif(operator=="*"):
    print("Result=",multiply(a,b))
 elif(operator=="/"):
    print("Result=",divide(a,b))
 elif(operator=="%"):
    print("Result=",mod(a,b))
 else:
    print("\nEnter a valid operation!")
 ch=int(input("\nPress 1 to continue or 0 to exit:"))
 if(ch):
    continue
 else:
    break  
