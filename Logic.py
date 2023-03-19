from threading import *

def btnthread(x):
    t=Thread(target=x)
    t.start()

def listtostr(tl):
    strg=""
    for x in tl:
        strg+=x[0]+", "
    return strg[0:len(strg)-2]

def tabinfo(n):
    l=[]
    for i in range(n):
       l.append("Round {}".format(i+1))
    l.append("Winners")
    return l
