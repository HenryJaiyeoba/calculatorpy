import re
import os.path

file_path = r"./equations.txt"
print(os.path.isfile(file_path))

def evaluate_func(x,y,op):
    if op == '+':
        answer = x+y
        print(f"The answer is {answer}")
        text = f"{x} {op} {y} = {answer}"
        result = [answer, text]
        return result
    elif op == '-':
        answer = x-y
        print(f"The answer is {answer}")
        text = f"{x} {op} {y} = {answer}"
        result = [answer, text]
        return result
    elif op == '*':
        answer = x*y
        print(f"The answer is {answer}")
        text = f"{x} {op} {y} = {answer}"
        result = [answer, text]
        return result
    elif op == '%':
        answer = x%y
        print(f"The answer is {answer}")
        text = f"{x} {op} {y} = {answer}"
        result = [answer, text]
        return result
    elif op == '/':
        try:
            answer = x / y
            print(f"The answer is {answer}")
            text = f"{x} {op} {y} = {answer}"
            result = [answer, text]
            return result
        except ZeroDivisionError as e:
            while y==0:
                print(f"Input a valid value for y that is not zero {e}")
                y = input("Please input a second number: ")
                # checking if it's a number
                if y.isdigit():
                    y = int(y)
                else:
                    print("y must be a valid number ")
                    y = input("Please input a second number: ")
                    checker(y)
            answer = x/y
            print(f"The answer is {answer}")
            text = f"{x} {op} {y} = {answer}"
            result = [answer, text]
            return result
    else:
        print("Please input a valid operator")

def calculate(x,y,op):
    answer = evaluate_func(x,y,op)
    
    with open("history.txt", "a") as file:
        file.write(f"{answer[1]}\n")
    return answer[0]

def checker(x):
    while not re.search('[0-9]', x):
        print("❗️Please input a valid number")
        x = input("Please input a first number: ")
    x = float(x)
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
    x = input("Please input a first number: ")
    x = checker(x)
    op = input("Please input an operator: ")

    y = input("Please input a second number: ")
    y = checker(y)

    calculate(x,y,op)

elif user_input == 'u':
    file_name = input("Please input the file name containing the arithmetic operations: ")
    # print(file_name) 
    try:
        with open(f"{file_name}.txt", "r") as file:
            line = file.read()
        # new_list = line.replace(",", "\n")
        new_list = line.replace("   ", "\n")
        new_list = re.split(',|\n|\.|#',new_list )
        # print(new_list)
        new_list = [el for el in new_list if el != ""]
        print(new_list)
        for id,el in enumerate(new_list):
            el = el.strip()
            el = el.replace(" ","")
            print(el)

            # print(f"checker{el}checker")
            
            if len(el) == 3:
                x = checker(el[0])
                op = el[1]
                y = checker(el[2])
                print(x,op,y)
                answer = calculate(x,y,op)
                print(answer)
            elif len(el)>3:
                answer = el[0]
                for i in range(0,len(el)-1,2):
                    x = checker(answer)
                    op = el[i+1]
                    y = checker(el[i+2])
                    answer = calculate(x,y,op)
                    answer = str(answer)
                    print(answer)
                    
                print(f"The answer is {answer}")

            # elif len(el) > 3:
            #     for id in range(0,len(el),2):
            #        print(id)
            #        checker(el[id])
            #     answer = eval(el)
            #     print(el)
            #     print(f"The answer is {answer}")
            else:
                print(el)
                print(f"The answer is {el}")

            # el.split("\n")
            # el = "".join(el.split())
            # print(el)
            # print(operation)
            # arg1 = operation[0]
            # op = operation[1]
            # arg2 = operation[2]
            # x = checker(arg1)
            # y = checker(arg2)
            # print(x,op,y)
            # answer = calculate(x,y,op)
            # if len(operation) > 3:
            #     op2 = operation[3]
            #     z = checker(operation[4])
            #     print(x,op,y,op2,z)
            #     calculate(answer,z,op2)
    except FileNotFoundError as er:
        print(er)
    




