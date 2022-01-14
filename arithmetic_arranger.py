import operator
import sys
from numpy.core.defchararray import isnumeric
import copy

def arithmetic_arranger(problems, check = False):
    myinput = problems
#Operators used in the calculations
    ops = {
        '+': operator.add,
        '-': operator.sub
    }
#Splitting the input into a list
    if len(myinput) > 5:
        raise ValueError("Error: Too many problems.")
    for i in range(len(myinput)):
        if myinput[i] == "":
            raise ValueError("Error: This is an invalid input")
        else:
            try:
                myinput[i] = myinput[i].split()

            except:
                raise ValueError("Error: This is an invalid input")
    myinputstr = copy.deepcopy(myinput)

#Converting numbers from string to in from the list as well as checking for the lenth of the digits
    for i in range(len(myinput)):
        for h in range(len(myinput[i])):
            num = myinput[i][h]
            if len(num) > 4:
                raise ValueError("Error: Numbers cannot be more than four digits.")
            else:
                if isnumeric(num) == True:
                    myinput[i][h] = int(myinput[i][h])

#Finding the total of the numbers provided
    allanswers = []
    for i in range(len(myinput)):
        k = 0
        total = 0
        while k < len(myinput[i]):
            if k < 3:
#Checking that the input is numeric
                try:
                    num1 = myinput[i][k]
                    num2 = myinput[i][k + 2]
                except:
                    raise ValueError("Error: This is an invalid input")
                if isinstance(num1, int) == True and isinstance(num2, int) == True:
#checking the operator is a + or - sign
                    try:
                        total = ops[myinput[i][k+1]](num1,num2)
                        k += 3
                    except:
                        raise ValueError("Error: Operator must be '+' or '-'")
                else:
                    raise ValueError("Error: Numbers must only contain digits")
            else:
# Checking that the input is numeric
                num3 = myinput[i][k + 1]
                if isinstance(num3, int) == True:
# checking the operator is a + or - sign
                    try:
                        total = ops[myinput[i][k]](total,num3)
                        k += 2
                    except:
                        raise ValueError("Error: Operator must be '+' or '-'")
                else:
                    raise ValueError("Error: Numbers must only contain digits")
        allanswers.append(total)

#printing the output
    testprnt = [[] * 1 for i in range(len(myinput))]
    for i in range(len(myinputstr)):
        k = 0
        num = max(myinputstr[i], key=len)
        line = len(num) +2
        while k < (len(myinputstr[i])):
            if k < 1:
                testprnt[i].append(myinputstr[i][k].rjust(line))
                k += 1
            else:
                testprnt[i].append((myinputstr[i][k]) + (myinputstr[i][k+1]).rjust(line-1))
                k += 2
        testprnt[i].append("-"*line)
        if check == True:
            testprnt[i].append(str(allanswers[i]).rjust(line))
#splitting the list into a new list with the columns in touples
    columns = list(zip(*testprnt))
    answer = ''
    for i in range(len(columns)):
        space = 1
        for k in columns[i]:
            if space != len(columns[i]):
                answer = answer + (k + '    ')
                space += 1
            else:
                answer = answer + k
                space += 1
        if (i+1) == len(columns):
            answer = answer
        else:
            answer = answer + '\n'

    arranged_problems = answer

    return arranged_problems
