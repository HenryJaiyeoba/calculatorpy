import re
import os.path

file_path = r"./equations.txt"
print(os.path.isfile(file_path))

def evaluate_func(x,y,op):
    if op == '+':
        answer = x+y
        text = f"{x} {op} {y} = {answer}"
        result = [answer, text]
        return result
    elif op == '-':
        answer = x-y
        text = f"{x} {op} {y} = {answer}"
        result = [answer, text]
        return result
    elif op == '*':
        answer = x*y    
        text = f"{x} {op} {y} = {answer}"
        result = [answer, text]
        return result
    elif op == '%':
        answer = x%y      
        text = f"{x} {op} {y} = {answer}"
        result = [answer, text]
        return result
    elif op == '/':
        try:
            answer = x / y
            text = f"{x} {op} {y} = {answer}"
            result = [answer, text]
            return result
        except ZeroDivisionError as e:
            while y==0:
                print(f"Input a valid second value that is not zero ")
                y = checker(input("Please input a second number: "))
            answer = x/y
            text = f"{x} {op} {y} = {answer}"
            result = [answer, text]
            return result
    else:
        print("Please input a valid operator")

def calculate(x,y,op):
    result = evaluate_func(x,y,op)
    
    with open("history.txt", "a") as file:
        file.write(f"{result[1]}\n")
    return result[0]

operators = ["+", "*", "-", "%", "/"]

def checker(x):
        while not re.search('[0-9]', x):
            print("❗️Please input a valid number")
            x = input("Please input a number: ")
        x = float(x)
        return x
def opchecker(x):
     while x not in operators:
            x = input("❕Please input a valid operator: ")
     return x

# History
user_input = input("Enter 'h' if you want to access the history \nEnter 'c' if you want to enter your own equation\nEnter 'u' if you want to upload your own .txt of operations to calculated\nEnter your choice: ")

if user_input == 'h':
    # read from history.txt
    with open("history.txt", "r") as file:
        for id,line in enumerate(file.readlines()):
            print(f"{id}. {line.rstrip()}")

elif user_input == 'c':
    # run calculate
    x = checker(input("Please input your first number: "))
    op = opchecker(input("Please input an operator: "))
    y = checker(input("Please input your second number: "))

    answer = calculate(x,y,op)
    print(f"The answer is {answer}")

elif user_input == 'u':
    file_name = input("Please input the file name containing the arithmetic operations: ")
    # print(file_name) 
    delimiter = r"(\+)|(\-)|(\*)|(\/)"
    try:
        with open(f"{file_name}.txt", "r") as file:
            line = file.read()
        # new_list = line.replace(",", "\n")
        new_list = line.replace("   ", "\n")
        new_list = re.split(',|\n|#',new_list )
        # print(new_list)
        new_list = [el for el in new_list if el != ""]
        # print(new_list)
        for el in new_list:
            el = el.strip()
            el = el.replace(" ","")
            print(f"Question: {el}")
            val = re.split(delimiter, el)
            val = [x for x in val if x is not None]
            # print(val)
            # print(f"checker{el}checker")
            
            if len(val) == 3:
                x = checker(val[0])
                op = opchecker(val[1])
                y = checker(val[2])
                answer = calculate(x,y,op)
                answer = float(answer)
                print(f"The answer is {answer:.2f}")
            elif len(val)>3:
                answer = val[0]
                for i in range(0,len(val)-1,2):
                    x = checker(answer)
                    op = val[i+1]
                    y = checker(val[i+2])
                    answer = calculate(x,y,op)
                    answer = str(answer)
                answer = float(answer)    
                print(f"The answer is {answer:.2f}")
            else:
                val = float(val)
                print(f"The answer is {val:.2f}")

    except FileNotFoundError as er:
        print(er)
    




