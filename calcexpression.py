def isOpreator(keyword):
    if(keyword == '+' or keyword == '-'or keyword == '*'or keyword == '/'or keyword == '(' or keyword == ')'):
        return 1
    else:
        return 0
def splitExpressionToKeyword(strExpression):
    result = []
    for charater in strExpression:
        if(isOpreator(charater)):
            result.append(charater)
        elif(len(result) != 0 and  0 == isOpreator(result[len(result) -1]) ):
            tmpstr = str(result.pop())
            tmpstr += charater
            result.append(tmpstr)
        else:
            result.append(charater)
        #print result
    return result
def convertMidToBackExpression(ExpressionList):
    stack1 = []
    stack2 = []
    for keyword in ExpressionList:
        if(not isOpreator(keyword)): 
            stack1.append(keyword)
        elif(keyword == "("):
            stack2.append(keyword)
        elif(keyword == ")"):
            while(0 != len(stack2) and stack2[len(stack2) - 1] != "("):
                stack1.append(stack2.pop())
            if (0 != len(stack2)):
                stack2.pop()
        elif(keyword == "+" or keyword == "-"):       
            while(len(stack2) != 0 and stack2[len(stack2) -1] != "/" and stack2[len(stack2) -1] != "*" and stack2[len(stack2) -1] != "("):
                stack1.append(stack2.pop())
            stack2.append(keyword)
        elif(keyword == "*" or keyword == "/"):
            if(0 != len(stack2)):
                stack2[len(stack2) -1] = stack2[len(stack2) -1]
            if(stack2[len(stack2) -1] == "+" and stack2[len(stack2) -1] != "-"):
                stack2.append(keyword)
            else:
                while(len(stack2) != 0 and (stack2[len(stack2) -1] != "+" and stack2[len(stack2) -1] != "-" and stack2[len(stack2) -1] != "(")):
                    stack1.append(stack2.pop())
                stack2.append(keyword)  
        else:
            stack2.append(keyword)
        #print "stack1" + str(stack1)
        #print "stack2" + str(stack2)
    while(0 != len(stack2)):
        stack1.append(stack2.pop())
    return stack1
def calcate(strOpraetor,num1,num2):
    if(strOpraetor == "+"):
        return num1 + num2
    elif(strOpraetor == "-"):
        return num1 - num2
    elif(strOpraetor == "*"):
        return num1 * num2    
    elif(strOpraetor == "/"):
        return num1 / num2
    else:
        print "calcate err"
        return 0
def calclExpression(ExpressionList):
    result = []
    for keyword in ExpressionList:
        if(isOpreator(keyword)):
            if(len(result) < 2):
                print "expression err"
            else:
                num2 = result.pop()
                num1 = result.pop()
                result.append(calcate(keyword, num1, num2))
        else:
            result.append(int(keyword))
        #print result
    if(len(result) == 1):
        return result[0]
    else:
        print "calclExpression err"
testexpression = "11+((22+23)*4)-50/(200/10)"
print calclExpression(convertMidToBackExpression(splitExpressionToKeyword(testexpression)))
            