from tkinter import*
from PIL import ImageTk,Image
import random

root = Tk()

root.title("POkemon_Game")
root.geometry("600x400")
root.configure(background = "red")



abra = ImageTk.PhotoImage(Image.open("abra.jpg"))
bulbasaur = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
chamandar = ImageTk.PhotoImage(Image.open("charmender.jpg"))
ivyasour = ImageTk.PhotoImage(Image.open("iyvasour.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
meowth = ImageTk.PhotoImage(Image.open("meowth.jpg"))
nidoking = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
paras = ImageTk.PhotoImage(Image.open("paras.jpg"))
persian = ImageTk.PhotoImage(Image.open("persion.jpg"))
pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
ratat = ImageTk.PhotoImage(Image.open("ratata.jpg"))
squirtle = ImageTk.PhotoImage(Image.open("squirtle.jpg"))
image_list = [abra,bulbasaur,chamandar,ivyasour,jigglypuff,kadabra,meowth,nidoking,paras,persian,pikachu,ratat,squirtle]
number_list = [30,60,50,100,70,70,60,90,40,70,200,40,50]



img = ImageTk.PhotoImage(Image.open("button.png"))
player1 = Label(root,bg="royal blue",fg="black",text="Player1")
player1.place(relx=0.1,rely=0.3,anchor=CENTER)

player1_score = Label(root,bg="yellow",fg="black")
player1_score.place(relx=0.1,rely=0.4,anchor=CENTER)


player2 = Label(root,bg="royal blue",fg="black",text="Player2")
player2.place(relx=0.8,rely=0.3,anchor=CENTER)

player2_score = Label(root,bg="yellow",fg="black")
player2_score.place(relx=0.8,rely=0.4,anchor=CENTER)

label = Label(root)
label.place(relx = 0.5,rely = 0.5,anchor=CENTER)

player1_score_val = 0
def player1_score_fun():
    global player1_score_val
    random1 = random.randint(0,12)
    random_img1 = image_list[random1]
    label["image"] = random_img1
    power_random = number_list[random1]
    player1_score_val = player1_score_val + power_random
    player1_score["text"] = "score = "+str(player1_score_val)

player1_btn = Button(root,image = img,command = player1_score_fun)
player1_btn.place(relx=0.1,rely=0.7,anchor=CENTER)

player2_score_val = 0
def player2_score_fun():
    global player2_score_val
    random2 = random.randint(0,12)
    random_img2 = image_list[random2]
    label["image"] = random_img2
    power_random = number_list[random2]
    player2_score_val = player2_score_val + power_random
    player2_score["text"] = "score = "+str(player2_score_val)

player2_btn = Button(root,image = img,command = player2_score_fun)
player2_btn.place(relx=0.8,rely=0.7,anchor=CENTER)

root.mainloop()
