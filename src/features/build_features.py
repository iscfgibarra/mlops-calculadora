import re


def parse_input(operation: str):
    reg_exp = r'(\d+.?\/?\d?)\s{0,10}(-|\+|\*|\/)\s{0,10}(\d+.?\/?\d?)'
    a = ""
    operator = ""
    b = ""

    match = re.match(reg_exp, operation)
    ok = match is not None
    if ok:
        numbers = re.findall(reg_exp, operation)
        a = numbers[0][0]
        operator = numbers[0][1]
        b = numbers[0][2]

    return ok, a, operator, b


def parse_float(operator: str):
    reg_exp = r'^(\d+)\/(\d+)'
    a = 0
    b = 0
    match = re.match(reg_exp, operator)
    if match is not None:
        numbers = re.findall(reg_exp, operator)
        a = float(numbers[0][0])
        b = float(numbers[0][1])
        return division(a, b)

    return float(operator)


def suma(a, b):
    return a + b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise Exception("el divisor no puede ser 0")

    return a / b


def resta(a, b):
    return a - b


def execute_operation(operation: str):
    ok, oper_a, op, oper_b = parse_input(operation)
    if ok:
        a = parse_float(oper_a)
        b = parse_float(oper_b)
        if op == "+":
            return suma(a, b)

        if op == "-":
            return resta(a, b)

        if op == "*":
            return multiplicacion(a, b)

        if op == "/":
            return division(a, b)
    else:
        raise Exception("no se puede ejecutar la operacion")


