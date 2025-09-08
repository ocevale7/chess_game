from affichage import luncher
from tkinter import *
from tkscrolledframe import ScrolledFrame
from PyQt5.QtWidgets import *

global screen_width
global screen_height

#screen = QApplication.screens()[0]
#screen_width = screen.width()
#screen_height = screen.height()

screen_width, screen_height = 1300,700

fenetre = Tk()

fenetre.title("Echec")
sf = ScrolledFrame(fenetre)
sf.pack(side='right',expand=1,fill="both")

sf.bind_arrow_keys(fenetre)
sf.bind_scroll_wheel(fenetre)

inner_frame = sf.display_widget(Frame)

aide = True
tourne = True
edit = False

def Aide_oui():
    global aide
    aide = True
    return None

def Aide_non():
    global aide
    aide = False
    return None

def Tourne_oui():
    global tourne
    tourne = True
    return None

def Tourne_non():
    global tourne
    tourne = False
    return None

def lanceur():
    fenetre.destroy()
    luncher(value1.get(),value2.get(),aide,var.get(),tourne,edit,(screen_width,screen_height))
    return None

def Edit_oui():
    global edit
    edit = True
    return None

def Edit_non():
    global edit
    edit = False
    return None



label_text1 = Label(inner_frame, text="Bonjour à vous ! Vous allez jouer aux echecs en 1vs1 !!")
label_text3 = Label(inner_frame, text="Vous devriez connaitre les règles des echecs mais, au cas ou, aucune triche ne sera validé par le programme, et vous pourrez activer une aide, ou non, pour vous aider à bouger les pièces.")
label_text4 = Label(inner_frame, text="Pour jouer, il faut cliquer avec la souris une première fois sur la pièce que tu veux jouer, puis une seconde sur l'endroit où tu veux la jouer.")
label_text5 = Label(inner_frame, text="Une fois une pièce jouée, tu ne peux pas revenir en arrière, donc fais attention !!")
label_text6 = Label(inner_frame, text="Parlons des points... ceux ci ne servent que ci vous voulez jouer avec un temps limiter, mais voici le recap :")
label_text7 = Label(inner_frame, text="Un pion vaut 1 point, un cavalier vaut 3 points, un fou vaut 3 points, une tour vaut 5 points, la dame vaut 9 points et le roi vaut la victoire !")
label_text8 = Label(inner_frame, text="Si tu amènes un pion au bout, tu ne pourras pas choisir une nouvelle pièce, ce pion disparaitra et te donnera 6 points.")
label_text9 = Label(inner_frame, text="Vous pouvez jouer contre un ordinateur, si c'est ce que vous voulez, laissez le nom 'Bot' dans une des deux cases.")
label_text91 = Label(inner_frame, text="Si vous voulez jouer à deux, changez ce nom par celui de votre adversaire.")

label_text1.pack()
label_text3.pack()
label_text4.pack()
label_text5.pack()
label_text6.pack()
label_text7.pack()
label_text8.pack()
label_text9.pack()
label_text91.pack()

value1 = StringVar()
value1.set("ecrire ici le pseudo du joueur 1")
value2 = StringVar()
value2.set("Bot")

label_text_nomBlanc = Label(inner_frame, text="Le pseudo du joueur qui joura les blancs :")
label_text_nomNoir = Label(inner_frame, text="Le pseudo du joueur qui joura les noirs :")

entree1 = Entry(inner_frame,textvariable=value1 ,width=30)
entree2 = Entry(inner_frame,textvariable=value2 ,width=30)
label_text_nomBlanc.pack()
entree1.pack()
label_text_nomNoir.pack()
entree2.pack()

label_text10 = Label(inner_frame, text="Voulez vous activer l'aider pour bouger les pièces (si vous n'appuyez sur aucun bouton, le programme considèrera une réponse positive) ?")

label_text10.pack()

bouton_oui_aide = Button(inner_frame, text = "oui", command = Aide_oui)
bouton_non_aide = Button(inner_frame, text = "non", command = Aide_non)

bouton_oui_aide.pack()
bouton_non_aide.pack()

label_text12 = Label(inner_frame, text="Voulez vous que l'échequier tourne automatiquement ? (par défault il le fait, et si le sens ne va pas, appuyez sur 't' ou sur la flèche qui tourne et il tournera)")

label_text12.pack()

bouton_oui_tourne = Button(inner_frame, text = "oui", command = Tourne_oui)
bouton_non_tourne = Button(inner_frame, text = "non", command = Tourne_non)

bouton_oui_tourne.pack()
bouton_non_tourne.pack()

label_text11 = Label(inner_frame, text="Difficulté du bot :")

label_text11.pack()

var = IntVar()
for item in range(1,10):
	rb = Radiobutton(inner_frame,text=str(item),value = item,variable = var)
	rb.pack()

label_text12 = Label(inner_frame, text="Dernière chose, avant de jouer voulez vous editer l'échiquier ? (par défaut mode normal)")

bouton_oui_edit = Button(inner_frame, text = "Editer", command = Edit_oui)
bouton_non_edit = Button(inner_frame, text = "Mode normal", command = Edit_non)

label_text12.pack()
bouton_oui_edit.pack()
bouton_non_edit.pack()

label_text14 = Label(inner_frame, text="Si tout est bon, appuyez sur ce dernier bouton !")
label_text14.pack()

bouton = Button(inner_frame, text = "Tout est bon ? Alors c'est parti...", command = lanceur)

bouton.pack()

fenetre.mainloop()
