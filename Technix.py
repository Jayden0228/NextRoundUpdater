from tkinter import *
from tkinter import ttk
import Gspread as gs

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

class TechApp(Tk):

    teamlist=[]
    
    def __init__(self):
        super().__init__()

        self.title("Technix 2023")
        self.geometry("900x500")

        mainframe=Frame(self)
        mainframe.pack()
        self.label=Label(mainframe, text="Select the Event!!", pady='20')
        self.label.config(font=("Courier", 16,"bold"))
        self.label.pack()

        self.clicked=StringVar()
        self.clicked.set("-- Select --")
        self.drop=OptionMenu(mainframe, self.clicked, *option)
        self.drop.config(width=len(max(option, key=len))+10, height=2)
        self.drop.pack()

        self.button=Button(mainframe, text=" Open ", command=lambda: [mainframe.destroy(), self.open()]).pack(pady='20')




    def add(self,i):
        tn=self.tree[i].selection()
        self.teamlist.append(self.tree[i].item(tn)['values'])
        print("List: ",self.teamlist)
    
    def remove(self,i):
        tn=self.tree[i].selection()
        if self.tree[i].item(tn)['values'] in self.teamlist:
            self.teamlist.remove(self.tree[i].item(tn)['values'])
        print("List: ",self.teamlist)






    def open(self):

        note=ttk.Notebook(self)
        note.pack()

        # Getting the total number of rounds in the event
        noOfRounds=eventinfo[self.clicked.get()][0]

        # Generating frames and adding it to the NoteBook
        frames=[]
        self.txtmg=[]
        self.tree=[]
        for i in range(noOfRounds+1):
            frames.append(Frame(note))
        
            frames[i].pack(fill="both", expand=1)

            if i!=noOfRounds:
                self.txtmg.append("Round {}".format(i+1))
            else:
                self.txtmg.append("Winners")


            self.tree.append(ttk.Treeview(frames[i],column=("c1"), show="headings", height=8))
            self.tree[i].column('c1', anchor="center")
            self.tree[i].heading('c1', text="Team Name")



            value=gs.read(eventinfo[self.clicked.get()][1], self.txtmg[i])
            for tname in value:
                self.tree[i].insert('','end', values=str(tname[0]))
            self.tree[i].pack()

            if i!=noOfRounds:
                #hardcoded value
                addbtn=Button(frames[i], text="Add", command=lambda: [self.add(0)])
                #hardcoded value
                rembtn=Button(frames[i], text="Remove", command=lambda: [self.remove(0)])
                #hardcoded value
                #Delete value of teamlist
                finbtn=Button(frames[i], text="Add To Next Round", command=lambda: [gs.write(eventinfo[self.clicked.get()][1], self.txtmg[1], self.teamlist)])
                addbtn.pack(pady=5)
                rembtn.pack(pady=5)
                finbtn.pack(pady=5)


            note.add(frames[i], text=self.txtmg[i])
        
        # print(noOfRounds)




if __name__=="__main__":
    app=TechApp()
    app.mainloop()