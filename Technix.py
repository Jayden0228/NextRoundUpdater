from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import Gspread as gs
from Logic import *

# img=ImageTk.PhotoImage('Technix.jpeg')

class TechApp(Tk):

    teamlist=[]
    
    def __init__(self):
        super().__init__()
        self.title("Technix 2023")
        self.geometry("900x550")
        self.mainpg()


    def mainpg(self):
         
        mainframe=Frame(self)
        mainframe.pack()
        
        self.img=ImageTk.PhotoImage(Image.open("Technix.png").resize((420,106), Image.ANTIALIAS))
        self.imglab=Label(mainframe, image=self.img)
        self.imglab.pack(pady='5')

        #Top text
        self.label=Label(mainframe, text="Select the Event!!", pady='20')
        self.label.config(font=("Courier", 16,"bold"))
        self.label.pack()

        #Drop down menu
        self.clicked=StringVar()
        self.clicked.set("-- Select --")
        self.drop=OptionMenu(mainframe, self.clicked, *option)
        self.drop.config(width=len(max(option, key=len))+10, height=2)
        self.drop.pack()

        #Button
        self.button=Button(mainframe, text=" Open ", command=lambda: [mainframe.destroy(), btnthread(self.open)]).pack(pady='20')


    #Adds the Team Name to the list
    def add(self):
        i=self.note.index(self.note.select())
        tn=self.tree[i].selection()
        teamname=self.tree[i].item(tn)['values']

        if teamname not in self.teamlist and teamname!='':
            self.teamlist.append(teamname)
            print("List: ",self.teamlist)
            self.label[i]['text']='Team List: '+ listtostr(self.teamlist)
    

    #Removes the Team Name from the list
    def remove(self):
        i=self.note.index(self.note.select())
        tn=self.tree[i].selection()
        teamname=self.tree[i].item(tn)['values']

        if teamname in self.teamlist:
            self.teamlist.remove(teamname)
            print("List: ",self.teamlist)
            self.label[i]['text']='Team List: '+ listtostr(self.teamlist)


    #Writes the Team Names That Moves to the Next Round
    def moveToNxtRnd(self, event):
        i=self.note.index(self.note.select())

        gs.write(eventinfo[event][1], self.txtmg[i+1], self.teamlist)

        self.teamlist=[]
        print("List: ",self.teamlist)
        self.label[i]['text']='Team List: '

        self.imglab.config(image='', pady=0)
        self.note.destroy()
        self.open()


    def open(self):

        self.img=ImageTk.PhotoImage(Image.open("Technix.png").resize((300,76), Image.ANTIALIAS))
        self.imglab=Label(self, image=self.img)
        self.imglab.pack(pady='9')

        self.note=ttk.Notebook(self)
        self.note.pack()

        # Getting the total number of rounds in the event
        event=self.clicked.get()
        noOfRounds=eventinfo[event][0]

        frames=[]
        self.txtmg=tabinfo(noOfRounds)
        self.tree=[]
        self.label=[]

        # Generating frames and adding it to the NoteBook
        for i in range(noOfRounds+1):

            frames.append(Frame(self.note, width=250, height=300))
            frames[i].pack(fill="both", expand=1)
            self.note.add(frames[i], text=self.txtmg[i])


            #Creating Treeview
            self.tree.append(ttk.Treeview(frames[i], column=("c1"), show="headings",  height=8))
            self.tree[i].column('c1', width=250, anchor="center")
            self.tree[i].heading('c1', text="Team Name")

            #Reading the Team Name and Displaying it
            value=gs.read(eventinfo[event][1], self.txtmg[i])
            for tname in value:
                self.tree[i].insert('','end', values=str(tname[0]))
            self.tree[i].pack()

            #Adding button for the rounds expect for the winners tab
            if i!=noOfRounds:
                addbtn=Button(frames[i], text="Add To The List", command=self.add).pack(pady=5)
                rembtn=Button(frames[i], text="Remove From The List", command=self.remove).pack(pady=5)
                finbtn=Button(frames[i], text="Add To Next Round", command=lambda: self.moveToNxtRnd(event)).pack(pady=5)

                canvas=Canvas(frames[i], height=10)
                canvas.create_line(0,10,1000,10,width=3)
                canvas.pack()
                self.label.append(Label(frames[i], text='Team List: '))
                self.label[i].pack(pady=5)
            


if __name__=="__main__":
    app=TechApp()
    app.mainloop()