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
        print("Error: Too many problems.")
        sys.exit()
    for i in range(len(myinput)):
        if myinput[i] == "":
            print("Error: This is an invalid input")
            sys.exit()
        else:
            try:
                myinput[i] = myinput[i].split()

            except:
                print("Error: This is an invalid input")
                sys.exit()
    myinputstr = copy.deepcopy(myinput)

#Converting numbers from string to in from the list as well as checking for the lenth of the digits
    for i in range(len(myinput)):
        for h in range(len(myinput[i])):
            num = myinput[i][h]
            if len(num) > 4:
                print("Error: Numbers cannot be more than four digits.")
                sys.exit()
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
                    print("Error: This is an invalid input")
                    sys.exit()
                if isinstance(num1, int) == True and isinstance(num2, int) == True:
#checking the operator is a + or - sign
                    try:
                        total = ops[myinput[i][k+1]](num1,num2)
                        k += 3
                    except:
                        print("Error: Operator must be '+' or '-'")
                        sys.exit()
                else:
                    print("Error: Numbers must only contain digits")
                    sys.exit()
            else:
# Checking that the input is numeric
                num3 = myinput[i][k + 1]
                if isinstance(num3, int) == True:
# checking the operator is a + or - sign
                    try:
                        total = ops[myinput[i][k]](total,num3)
                        k += 2
                    except:
                        print("Error: Operator must be '+' or '-'")
                        sys.exit()
                else:
                    print("Error: Numbers must only contain digits")
                    sys.exit()
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
        answer = answer + ''
        for k in columns[i]:
            answer = answer + (k + '\t\t')
        answer = answer + '\n'

    arranged_problems = answer

    return arranged_problems
