def arithmetic_arranger(problems, display=False):
    
    operators = []
    longestOperands = []
    lenthDiff = []

    numSpace = []

    printList = []
    printList2 = []
    printList3 = []

    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in range(len(problems)):
        if "+" in problems[problem]:
            problems[problem] = problems[problem].split(" + ")
            operators.append("+")
            
        elif "-" in problems[problem]:
            problems[problem] = problems[problem].split(" - ")
            operators.append("-")

        else:
            return "Error: Operator must be '+' or '-'."

    for problem in range(len(problems)):
        if problems[problem][0].isdigit() == False or problems[problem][1].isdigit() == False:
            return "Error: Numbers must only contain digits."


    for problem in range(len(problems)):
        if len(problems[problem][0]) > 4 or len(problems[problem][1]) > 4:
            return "Error: Numbers cannot be more than four digits."


    for problem in range(len(problems)):
        if len(problems[problem][0]) < len(problems[problem][1]):
            longestOperands.append("1")

            lenthDiff.append(1 + (len(problems[problem][1])-len(problems[problem][0])))
        else:
            longestOperands.append("-1")

            lenthDiff.append(-1 - (len(problems[problem][0])-len(problems[problem][1])))

    for lens in range(len(lenthDiff)):
        if lenthDiff[lens] > 0:
            for num_times_print in range(lenthDiff[lens]):
                printList.append(" ")
            printList.append(" ")
            printList.append(problems[lens][0])

            if lens != (len(problems) - 1):
                printList.append("    ")
        else:
            printList.append("  ")
            printList.append(problems[lens][0])

            if lens != (len(problems) - 1):
                printList.append("    ")

    for lens in range(len(lenthDiff)):
        printList2.append(operators[lens])
        if lenthDiff[lens] < 0:
            for spaces in range(abs(lenthDiff[lens])):
                printList2.append(" ")
            printList2.append(problems[lens][1])

            if lens != (len(problems) - 1):
                printList2.append("    ")
        else:
            printList2.append(" ")
            printList2.append(problems[lens][1])

            if lens != (len(problems) - 1):
                printList2.append("    ")

    for operands in range(len(longestOperands)):
        if longestOperands[operands] == "-1":
            for number_of_dashes in range(len(problems[operands][0])+2):
                printList3.append("-")
        else:
            for number_of_dashes in range(len(problems[operands][1])+2):
                printList3.append("-")
                

        if operands != (len(problems) - 1):
            printList3.append("    ")

    x = ''.join(printList) + "\n" + ''.join(printList2) + "\n" + ''.join(printList3)
    
    if display == True:
        solutions = []
        printList_4 = []
        for problem in range(len(problems)):
            if operators[problem] == "+":
                solutions.append(int(problems[problem][0]) + int(problems[problem][1]))
            else:
                solutions.append(int(problems[problem][0]) - int(problems[problem][1]))

        for problem in range(len(problems)):
            if len(problems[problem][0]) > len(problems[problem][1]):
                numSpace.append(len(str(problems[problem][0])) - len(str(solutions[problem])))
            else:
                numSpace.append(len(str(problems[problem][1])) - len(str(solutions[problem])))

        for spaces in range(len(numSpace)):
            for i in range(2 + int(numSpace[spaces])):
                printList_4.append(" ")
                
            printList_4.append(solutions[spaces])

            if spaces != (len(problems) - 1):
                printList_4.append("    ")

        for i in range(len(printList_4)):
            if isinstance(printList_4[i], int):
                printList_4[i] = str(printList_4[i])

        x = ''.join(printList) + "\n" + ''.join(printList2) + "\n" + ''.join(printList3) + "\n" + ''.join(printList_4)
            
        return x

    else:
        return x