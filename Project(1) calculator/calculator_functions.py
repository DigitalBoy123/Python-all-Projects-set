 # In this file we will control the mathematical operations of this project.
def add_num(a, b):
    return a + b
def sub_num(a, b):
    return a - b
def mul_num(a, b):
    return a * b
def div_num(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
def mod_num(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a % b
def pow_num(a, b):
    return a ** b
def sqrt_num(a):
    if a < 0:
        return "Error: Square root of negative number"
    return a ** 0.5
def cube_num(a):
    return a ** 3
def cube_root_num(a):
    if a < 0:
        return "Error: Cube root of negative number"
    return a ** (1/3)
def factorial_num(a):
    if a < 0:
        return "Error: Factorial of negative number"
    if a == 0 or a == 1:
        return 1
    result = 1
    for i in range(2, a + 1):
        result *= i
    return result
def square_num(a):
    return a ** 2

def table_of_num(a):
    table = ""
    for i in range(1,11):
        table += f"{a} X {i} = {a*i}\n"
    return table


 



