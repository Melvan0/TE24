

def add():
    return n+m

def subs():
    return n-m

def prod():
    return n*m

def div():
    return m/n

def operations(op):
    switch={
       '+', "add": 
            add(),
       '-', "subtract": subs(),
       '*',"multiply": prod(),
       '/', "divide": div(),
       }
    return switch.get(op,'Choose one of the following operator:+,-,*,/,')

