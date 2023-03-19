from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from googleapiclient.errors import HttpError
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

    # Main Frame Page
    def mainpg(self):
         
        mainframe=Frame(self)
        mainframe.pack()
        
        #Technix Image
        self.img=ImageTk.PhotoImage(Image.open("Technix.png").resize((420,134), Image.ANTIALIAS))
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

        #Deleting the Childrens of Old Tree View
        for item in self.tree[i+1].get_children():
            self.tree[i+1].delete(item)

        #Reading the New Team Name and Displaying it (Updated TreeView)
        value=gs.read(eventinfo[event][1], self.txtmg[i+1])
        for tname in value:
            self.tree[i+1].insert('','end', values=str(tname[0]))
        self.tree[i+1].pack()


    # Displays the Event Frame 
    def open(self):
        self.eventframe=Frame(self)
        self.eventframe.pack()

        # Back Button
        self.back=Button(self, text='Back', command=lambda:[self.eventframe.destroy(), self.mainpg(), self.back.destroy()])
        self.back.place(x=70,y=30)

        # Technix Image
        self.img=ImageTk.PhotoImage(Image.open("Technix.png").resize((300,105), Image.ANTIALIAS))
        self.imglab=Label(self.eventframe, image=self.img)
        self.imglab.pack(pady='12')

        try:
            self.note=ttk.Notebook(self.eventframe)
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

                #Frames created and Added kto the notebook
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

                # Adding button for the rounds expect for the winners tab
                if i!=noOfRounds:
                    Button(frames[i], text="Add To The List", command=self.add).pack(pady=5)
                    Button(frames[i], text="Remove From The List", command=self.remove).pack(pady=5)
                    Button(frames[i], text="Add To Next Round", command=lambda: self.moveToNxtRnd(event)).pack(pady=5)
                    # Button(frames[i], text="Add To Next Round", command=lambda: [btnthreadarg(self.moveToNxtRnd, (event))] ).pack(pady=5)

                    # Horizontal Line
                    canvas=Canvas(frames[i], height=10)
                    canvas.create_line(0,10,1000,10,width=3)
                    canvas.pack()

                    # Displays list of Team Names selected
                    self.label.append(Label(frames[i], text='Team List: '))
                    self.label[i].pack(pady=5)
        
        except HttpError as err:
            self.note.destroy()
            self.label=Label(self.eventframe, text="Unable to find the google sheet. Please check your internet connection or the google sheet Id")
            self.label.config(font=("Times", 13))
            self.label.pack(pady=40)

        except (UnboundLocalError, TypeError):
            self.note.destroy()
            self.label=Label(self.eventframe, text="Variable is accessed before assignment")
            self.label.config(font=("Times", 13))
            self.label.pack(pady=40)

        except Exception as err:
            self.label=Label(self.eventframe, text="Error Occured!!")
            self.label.config(font=("Times", 13))
            self.label.pack(pady=40)
            print(f"Unexpected {err=}, {type(err)=}")


if __name__=="__main__":
    app=TechApp()
    app.mainloop()