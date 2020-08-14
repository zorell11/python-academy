
def check(prem):
    sum = 0

    for i in prem:
        if i in '([{}':
            sum +=1
        elif i in ')]}':

            sum -=1
    if sum == 0:
        return True
    else:
        return False

expr = "5 + (a - b) * (64-2) + 5)"
print(check(expr))

expr = "{'name':'John', 'address' : {'street':'Main', 'City':'London','number':123}, 'performance': [3,1,2,1,1]}"
print(check(expr))


#### riesenie z hodiny:

def check1(expr):
    brackets = {'(':')', '{':'}','[':']'}
    stack = ['']

    for char in expr:

        if char in brackets:
            stack.append(brackets[char])

        elif char in brackets.values() and char != stack.pop():
            return False

    return stack == ['']


expr = "{'name':'John', 'address' : {'street':'Main', 'City':'London','number':123}, 'performance': [3,1,2,1,1]}"
print(check1(expr))
