def codeNum (codeStr):
    if len(codeStr) == 0:
        return 1
    
    sum = 0
    code1, newCodeStr1 = codeStr[0:1], codeStr[1:]
    code2, newCodeStr2 = codeStr[0:2], codeStr[2:]
    
    for i in range(1,27):
        if i // 10 == 0:
            if int(code1) == i:
                sum += codeNum(newCodeStr1)
        else:
            if int(code2) == i:
                sum += codeNum(newCodeStr2)
        
    return sum
    
print(codeNum("121212"))

def codeNum2 (codeStr):
    
    if len(codeStr) == 0:
        return 0
    
    matchNum = [1]
    lastCode = ''
    
    for i in range(len(codeStr)):
        
        code, codeStr = codeStr[0:1], codeStr[1:]
        if code == '0':
            return 0
        
        if i == 1:
            matchNum.append(2 if int(lastCode + code) <= 26 else 1)
            
        if i >= 2:
            matchNum.append(matchNum[i-1] + (matchNum[i-2] if int(lastCode + code) <= 26 else 0))
        
        lastCode = code
        
    return matchNum.pop()
	
print(codeNum2("121212"))