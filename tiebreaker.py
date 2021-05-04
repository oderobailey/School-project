from graphics import*
import random
#new window
myWindow = GraphWin('Tie Breaker',1000,350)
mymsg = Text(Point(500,40),'Trouble deciding who gets the last piece of candy bar? Use this tool to help.'#create messgae,store in my msg
mymsg.draw(myWindow) #draw messgae in window
entry1 = Entry(Point(500,110),10) #create entry box in entry1
entry1.draw(myWindow) #display entry box
    Text(Point(500-225,110),'First person, guess a number between 1 and 10').draw(myWindow)
entry2 = Entry(Point(500,110),10) #create entry box in entry2
entry2.draw(myWindow) #display entry box
    Text(Point(500-225,110),'Second person, guess a number between 1 and 10').draw(myWindow)
myWindow.getMouse() #use mouse to start program
#get guesses
q1 = entry1.getText()
q2 = entry2.getText()
ran_num = random.randint(1,10) #random number bwtween 1 and 10
number1 = int(q1)
number2 = int(q2)
difference1 = number1-ran_num
difference2 = number2-ran_num
abs_difference1 = abs(difernce1)
abs_difference2 = abs(difernce2)
#test the winner
if abs_difference1<abs_difference2:
    out = 'The first person gets the candy bar!'
elif abs_difference1>abs_difference2:
    out = 'The second person gets the candy bar!'
else:
    out = 'Tie, split the candy bar.'
msg3 = Text(Point(500,300),out)
msg3.draw(myWindow)
