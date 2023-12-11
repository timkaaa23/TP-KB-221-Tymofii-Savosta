def infix_to_postfix(expression):
    output = []  
    stack = []   

    precedence = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}

    for symbol in expression:
        if symbol.isalnum():
            output.append(symbol)
        elif symbol == '(':
            stack.append(symbol)
        elif symbol == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  
        else:
            while stack and precedence[symbol] <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(symbol)

    while stack:
        output.append(stack.pop())

    return output

def evaluate_postfix(postfix_expression):
    stack = []

    for symbol in postfix_expression:
        if symbol.isalnum():
            stack.append(float(symbol))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if symbol == '+':
                result = operand1 + operand2
            elif symbol == '-':
                result = operand1 - operand2
            elif symbol == '*':
                result = operand1 * operand2
            elif symbol == '/':
                result = operand1 / operand2
            elif symbol == '^':
                result = operand1 ** operand2


            stack.append(result)

    return stack[0]

infix_expression = input('Enter an expression: ').split()
postfix_expression = infix_to_postfix(infix_expression)
result = evaluate_postfix(postfix_expression)

print(f"Entered expression: {infix_expression}")
print(f"RPN: {' '.join(postfix_expression)}")
print(f"Result: {result}")