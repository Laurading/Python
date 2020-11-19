from tkinter import *
from tkinter import ttk
from random import randint
import time

root = Tk()
player = {"level": 10, "score": 0, 'NbLine': 0}

cheight = 700
cwidth = 500
root.title("Game Mike")
root.resizable(False, False)

canvas = Canvas(root, width = cwidth, height = cheight)
canvas.pack()

# 1 - 10 => 2
# 11 - 15 => 3
# 16 - 18 => 4
# 19 - 20 => 5
# Tout les 10 line level++

def generateBlock():
    global canvas, cheight
    positionDepartX = randint(0, 9)*35
    positionFinalX = positionDepartX + 35
    positionDepartY = 0
    positionFinalY = 35

    couleur = ["red", "green", "blue", "gray"]
    color = couleur[randint(0, 3)]
    
    forme = canvas.create_rectangle(positionDepartX,positionDepartY, positionFinalX,positionFinalY, fill=color, tags='block')

    for x in range(700):
        
        myForme = canvas.coords(forme)
        prevForme = canvas.find_overlapping(myForme[0]+1,myForme[1],myForme[2]-1,myForme[3]) 
        if len(prevForme) > 1:
            print(myForme[3])
            print(prevForme)
            break
        
        if canvas.coords(forme)[1] > 665:
            break
        
        canvas.move(forme, 0, 1)


        def leftKey(event):
            prevForme = canvas.find_overlapping(myForme[0]-1,myForme[1],myForme[2]-1,myForme[3]) 
            if canvas.coords(forme)[0] > 0 and len(prevForme) == 1:
               canvas.move(forme,-35, 0 ) 

        def rightKey(event):
            prevForme = canvas.find_overlapping(myForme[0]+1,myForme[1],myForme[2]+1,myForme[3])
            if canvas.coords(forme)[0] < 315 and len(prevForme) == 1:
               canvas.move(forme,35, 0 )
        
        def downKey(event):
            if canvas.coords(forme)[1] < 665:
                prevForme = canvas.find_overlapping(myForme[0]+1,myForme[1],myForme[2]-1,myForme[3]+25) 
                
                if (canvas.coords(forme)[1] + 25) > 665 and len(prevForme) == 1:
                    canvas.move(forme,0, 665 - canvas.coords(forme)[1] )
                elif len(prevForme) == 1:
                    canvas.move(forme,0, 25 )

            
        root.bind('<Left>', leftKey)
        root.bind('<Right>', rightKey)
        root.bind('<Down>', downKey)

        root.update()

    generateBlock()
    
def createdWindows():
    global canvas

    canvas.create_rectangle(350, 0, 500, 700, fill= 'black')
    scoreText = canvas.create_text(390, 20, text="Score User: ", fill='white')
    scoreValeurText = canvas.create_text(465, 20, text="0pts", fill='white', font='bold')
    levelText = canvas.create_text(390, 50, text="Level User: ", fill='white')
    levelValeurText = canvas.create_text(465, 50, text="0", fill='white', font='bold') 
    generateBlock()

# canvas.itemconfig(levelValeurText, text = str(player['level']))

createdWindows()
root.mainloop()



