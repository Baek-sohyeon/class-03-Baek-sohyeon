from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):

    try:
        n = int(numStr)
    except:
        return 'Error!'

    if n>= 4000:
        return 'Error!'


    romans = {
        1000:'M', 900:'CM', 500:'D', 400:'CD',
        100:'C', 90:'XC', 50:'L', 40:'XL',
        10:'X', 9:'IX', 5:'V', 4:'IV',
        1:'I'
    }

    result = ""
    for value in sorted(romans.keys(),reverse = True):
        while n>= value:
            result += romans[value]
            n-=value
    return result


def RomanTodec(Str):
    numStr = Str
    n = 0
    while len(numStr)>0:
        if numStr.find('M')==0:
            n += 1000
            numStr=numStr.replace('M',"",1)
        else:
            if numStr.find('CM')==0:
                n+=900
                numStr=numStr.replace('CM',"",1)
            else:
                if numStr.find('D')==0:
                    n+=500
                    numStr=numStr.replace('D',"",1)
                else:
                    if numStr.find('CD') == 0:
                        n += 400
                        numStr=numStr.replace('CD', "", 1)
                    else:
                        if numStr.find('C') == 0:
                            n += 100
                            numStr=numStr.replace('C', "", 1)
                        else:
                            if numStr.find('XC') == 0:
                                n += 90
                                numStr=numStr.replace('XC', "", 1)
                            else:
                                if numStr.find('L') == 0:
                                    n += 50
                                    numStr=numStr.replace('L', "", 1)
                                else:
                                    if numStr.find('XL') == 0:
                                        n += 40
                                        numStr=numStr.replace('XL', "", 1)
                                    else:
                                        if numStr.find('X') == 0:
                                            n += 10
                                            numStr=numStr.replace('X', "", 1)
                                        else:
                                            if numStr.find('IX') == 0:
                                                n += 9
                                                numStr=numStr.replace('IX', "", 1)
                                            else:
                                                if numStr.find('V') == 0:
                                                    n += 5
                                                    numStr=numStr.replace('V', "", 1)
                                                else:
                                                    if numStr.find('IV') == 0:
                                                        n += 4
                                                        numStr=numStr.replace('IV', "", 1)
                                                    else:
                                                        if numStr.find('I') ==0:
                                                            n+=1
                                                            numStr=numStr.replace('I',"",1)

    return n

