import tkinter.messagebox
import tkinter
from random import randint
tplayer = 0
tcomp = 0
player = 0
comp = 0
master = tkinter.Tk()

def Tak():
   global player
   global comp
   tplayer = randint(1,6)
   tcomp = randint(1,6)
   message =""

   if tplayer>tcomp:
      message = "Wygrałeś!!!"
      player+=1
      tkinter.messagebox.showinfo("Tabela wyników","Ty: " + str(player) + "     Komputer: " + str(comp) + "\nWylosowałeś " + str(tplayer) + "\n" + "Komputer wylosował " + str(tcomp) + "\n" + message)
   elif tplayer==tcomp:
      message = "Remis"
      tkinter.messagebox.showinfo("Tabela wyników","Ty: " + str(player) + "     Komputer: " + str(comp) + "\nWylosowałeś " + str(tplayer) + "\n" + "Komputer wylosował " + str(tcomp) + "\n" + message)
   else:
      message = "Przegrałeś :("
      comp +=1
      tkinter.messagebox.showinfo( "Tabela wyników", "Ty: "+str(player) +"     Komputer: "+str(comp)+"\nWylosowałeś "+str(tplayer)+"\n"+"Komputer wylosował "+str(tcomp)+"\n"+message)
def Nie():
    master.quit()
master.geometry('360x70')
w = tkinter.Label(master,text = "Rzucić kostką?",font=("Helvetica", 20),fg="green")
Button1 = tkinter.Button(master, text ="Tak", command = Tak,width = 20)
Button2 = tkinter.Button(master, text = "Nie", command = Nie,width = 20)
w.grid(row = 0,column = 0)
Button1.grid(row = 1, column = 0)
Button2.grid(row = 1, column = 1)
master.mainloop()




















































