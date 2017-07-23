# method converts a base-10 integer to any base
def decToBase(num, base):
    result=[]
    if base>10:
        dic={}
        for i in range(10,36):
            dic[i]=chr(55+i)
        for i in range(36,62):
            dic[i]=chr(60+i)
    while (num>0):
        temp=num%base
        if temp>9:
            result.append(str(dic[num%base]))
        else:
            result.append(str(num%base))
        num=num//base
    result=list(reversed(result))
    return "".join(result)

# method converts a number of any base to a base-10 integer
def baseToDec(num, base):
    number=list(str(num))
    result=0
    for i in range(0, len(number)):
        result=result+(int(number[i])*base**(len(number)-i-1))
    return result
