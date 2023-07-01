from tkinter import *
import random
rps = Tk()
rps.geometry("300x300")
rps.title("Stone Paper Scissor")

user_score = 0
comp_score = 0
user_choice = --
comp_choice = --

def choice_to_no(choice):
    rps = {'Stone':0,'Paper':1,'Scissor':2}

def no_to_choice(number):
    rps = {0:'Stone',1:'Paper',2:'Scissor'}

def random_computer_choice():
    return random.choice(['Stone','Paper','Scissor'])

def result(human_choice,comp_choice):
    global user_score
    global comp_score
    user = choice_to_no(human_choice)
    comp = choice_to_no(comp_choice)
    if(user == comp):
        print("Draw")
    elif((user-comp)%3 == 1):
        print("You Win")
        user_score == 1
    else:
        print("Computer Wins")
        comp_score = comp_choice +1
    text_area = Text(master = rps, font = ("arial",20,"italic bold"), relief = RIDGE, bg = "orange", fg = "white", width = 20)
    text_area.grid(column = 0, row = 4)
    answer = "Your Choice : {uc} \nComputer's Choice : {cc} \nYour Score : {u} \nComputer Score : {c}".format(uc = user_choice, cc = comp_choice, u = user_score, c = comp_score)
    text_area.insert(END,answer)

def stone():
    global user_choice
    global comp_choice
    user_choice = "Stone"
    comp_choice = random_computer_choice()
    result(user_choice,comp_choice)

def paper():
    global user_choice
    global comp_choice
    user_choice = "Paper"
    comp_choice = random_computer_choice()
    result(user_choice,comp_choice)

def scissor():
    global user_choice
    global comp_choice
    user_choice = "Scissor"
    comp_choice = random_computer_choice()
    result(user_choice,comp_choice)

button_Stone = Button(text="    STONE   ",bg = "green", font = ("arial",15,"italic bold"), relirf = RIDGE, activebackground= "blue", activeforeground= "white", width = 24)
button_Stone.grid(column= 0, row= 1)

button_Paper = Button(text="    STONE   ",bg = "green", font = ("arial",15,"italic bold"), relirf = RIDGE, activebackground= "blue", activeforeground= "white", width = 24)
button_Paper.grid(column= 0, row= 1)

button_Sci = Button(text="    STONE   ",bg = "green", font = ("arial",15,"italic bold"), relirf = RIDGE, activebackground= "blue", activeforeground= "white", width = 24)
button_Stone.grid(column= 0, row= 1)