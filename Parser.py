def S():
    if P():
        return True
    
    elif D():
        return True
    
    elif O():
        return True
    
    elif I():
        return True
    
    elif T():
        return True
    
    elif C():
        return True
    
    return False

def Sprime():
    if S():
        return True
    else:
        return True

def P():
    if "r":
        if(Pprime()):
            if(";"):
                if Sprime():
                    return True
    return False

def Pprime():
    if'"':
        if w():
            if('"'):
                return True
    elif T():
        if var():
            return True
        
    return False

def w():
    if"w":
        return True
    return False

def T():
    if"int":
        return True
    return False

def var():
    if("var"):
        return True
    return False

def I():
    if b():
        if T():
            if var():
                return True
    return False

def b():
    if "b":
        return True
    return False

def O():
    if f():
        if "(":
            if d():
                if OP():
                    if d():
                        if ")":
                            if ";":
                                return True

    return False

def f():
    if "f":
        return True
    return False 

def d():
    if "d":
        return True
    return False

def OP():
    if plus():
        return True
    elif minus():
        return True
    elif multiply():
        return True
    elif divide():
        return True
    
    return False

def plus():
    if "+":
        return True
    return False

def minus():
    if "-":
        return True
    return False

def multiply():
    if "*":
        return True
    return False

def divide():
    if "/":
        return True
    return False

def D():
    if g():
        if T():
            if var():
                if A():
                    if ";":
                        if Sprime():
                            return True
    return False

def g():
    if "g":
        return True
    return False

def A():
    if "=":
        if Aprime():
            return True
        else:
            return False
    else:
        return True


def Aprime():
    if O():
        return True
    elif d():
        return True
    elif T():
        if var():
            return True
    return False


def C():
    if H():
        if Hprime():
            return True
    return False

def H():
    if h():
        if "(":
            if var():
                if "=":
                    if d():
                        if ")":
                            if B():
                                return True
    return False

def h():
    if "h":
        return True
    return False

def Hprime():
    if E():
        if Mprime():
            return True
        
    return False

def E():
    if e():
        if "(":
            if var():
                if "=":
                    if d():
                        if ")":
                            if B():
                                if Eprime():
                                    return True
    return False

def Eprime():
    if E():
        return True
    else:
        return True

def e():
    if "e":
        return True
    return False

def Mprime():
    if M():
        return True
    else: 
        return True


def M(): 
    if m():
        if B():
            return True
    return False

def m():
    if "m":
        return True
    return False

def B():
    if "{":
        if Bprime():
            if "}":
                return True
    return False

def Bprime():
    if S():
        if ";":
            if F():
                return True
    return False

def F():
    if S():
        if ";":
            if Fprime():
                return True
    return False

def Fprime():
    if F():
        return True
    else:
        return True



