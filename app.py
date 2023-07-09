import re

def calculate(x,y,op):
    if not( x or y or op):
        raise ValueError("A value or operator must be inputed")

    if(op == '+'):
        print(x + y)
    elif(op == "-"):
        print(x-y)
    elif(op == '*'):
        print(x*y)
    elif(op == "%"):
        print(x%y)
    elif(op == '/'):
        if y != 0:
            print(x/y)
        else:
            raise ZeroDivisionError("Divison by zero not allowed ")
    else:
        # Method one for operator checking
        # try:
        #     print("Please input a valid operator")
        #     op = input("Please input an operator")
        # except:
        #     pass
        # finally:
        #     calculate(x,y,op)
        print("This is an invalid operator")
        
operators = ['+','-','*','/','%']

# def raise_except ():
#     try: 
#         x = int(input("Please input a number"))
#         return True
#     except ValueError:
#         print("Please a number must be inputed")
#         return False
    
# while True:
#     if raise_except():
#         break
#     else:
#         continue
# x = input("Please input a number: ")
# y = input("Please input a number")
# op = input("Please input an op")



def inp():
    x = input("Please input a number for x: ")
    y = input("Please input a number for y: ")
    op = input("Please input an op: ")
    while not x.isdigit():
        print("Enter a number for x")
        x = input("Please input a number for x: ")
    x = int(x)
    while not y.isdigit():
        print("Enter a number for y")
        y = input("Please input a number for y: ")
    y = int(y)

    return x,y,op

# second method
def inputs():
    x = input("Please input a number for x: ")
    y = input("Please input a number for y: ")
    op = input("Please input an op: ")
    try:
        x = int(x)
        y = int(y)
    except:
        if not isinstance(x, int):
            print("x is probably the problem")
            while not isinstance(x,int):
                x = input("Please input a number for x again: ")
                try:
                    x = int(x)
                except:
                    pass
                finally:
                    try:
                        y = int(y)
                    except:
                        pass
        if not isinstance(y, int):
            print("y is probably the problem")
            while not isinstance(y,int):
                y = input("Please input a number for y again: ")
                try:
                    y = int(y)
                except:
                    pass


    
    return x,y,op

# third method
def inpt():
    x = input("Please input a number for x: ")
    y = input("Please input a number for y: ")
    op = input("Please input an op: ")
    while not re.search("[0-9]", x):
        print("Enter a number for x")
        x = input("Please input a number for x: ")
    x = int(x)
    while not re.search("[0-9]", y):
        print("Enter a number for y")
        y = input("Please input a number for y: ")
    y = int(y)
    # Method 2 for operator checking
    while op not in operators:
        print("❗️Please input a valid operator")
        op = input('Please input an operator: ')
    return x,y,op


x,y,op = inpt()
calculate(x,y,op)

# if isinstance(x, int):
#     print("Int")
# else:
#     print("Not string")
# checker = 0
# while checker == 0:
#     try:
#         x = int(input("Please input a number"))
#         y = int(input("Please input a number"))
#         op = input("Please input an operator")
#         checker = 1
#     except ValueError:
#         print("Please a number or operator must be inputed")
#         checker = 0




# if isinstance(y,):
#     print("I be Integer oooooooooooooo")

# calculate(x,y,op)
