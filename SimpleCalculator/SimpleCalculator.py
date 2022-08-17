import operator
import re

print("Welcome to calculator 2022\n")
print("First build supports + - * / ^\n")

ops = {"+": operator.add,
       "-": operator.sub,
       "*": operator.mul,
       "/": operator.truediv,
       "^": operator.pow}


again = True

def doCalc(opr):
    total = ops[opr](num1,num2)
    return total

while again:

    exp =input("Write your equation: ")
    oper = re.findall(r'[+-/*^]', exp)
    oper = ''.join(oper)


    part_num = exp.partition(''.join(oper))
    num1 = part_num[0]
    num1 = int(num1)
    num2 = part_num[2]
    num2 = int(num2)



    result = doCalc(oper)
    print("The result is: " + str(result))
    next = input("Do another(y/n)? ")
    print("--------------------------------------")
    if next == 'n':
     again = False
     print("Thank you for using my product")
