from threading import *

option=["Competitive_Coding",
        "Code_In_Chaos",
        "Hackathon",
        "TechQuiz",
        "Escape_Room",
        "Ideathon",
        "UI/UX_Design_Challenge",
        "Treasure_Hunt",
        "Speed_Typing",
        "Minecraft",
        "FIFA",
        "Reel_Making",
        "Photography",
        "Meme"
        ]

eventinfo={"Competitive_Coding":[3,''],
        "Code_In_Chaos":[3,''],
        "Hackathon":[3,''],
        "TechQuiz":[3,''],
        "Escape_Room":[3,''],
        "Ideathon":[3,''],
        "UI/UX_Design_Challenge":[3,''],
        "Treasure_Hunt":[3,'1hqy6DJIA1F__bU21gByCBasToU_krenNGFycd3nCrpk'],
        "Speed_Typing":[3,''],
        "Minecraft":[3,''],
        "FIFA":[3,''],
        "Reel_Making":[3,''],
        "Photography":[3,''],
        "Meme":[3,'']
        }

def btnthread(x):
    t=Thread(target=x)
    t.start()

def btnthreadarg(x, arg):
    t=Thread(target=x, args=arg)
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
