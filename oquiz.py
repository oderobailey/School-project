from graphics import*
import random
#new window
myWindow = GraphWin('Nfl Quiz',1000,350)
mymsg = Text(Point(500,40),'Take this quick quiz about the nfl.'#create messgae,store in my msg
mymsg.draw(myWindow) #draw messgae in window
#quiz start
q1 = input("Question 1: How many teams are in the NFL?")
q2 = input("Question 2: Which franchise has the most championships?")
q3 = input("Question 3: Who is the NFL leading td leader?")
q4 = input("Question 4: Who was the NFL 2019 MVP?")
q5 = input("Question 5: Who was the superbowl winners of the 2019 season?")
#question
if q1=="32":
    q1point = 1
    q1response = ""
else:
    q1response = "There are currently 32 NFL franchise"
    q1point = 0
if q2=="Steelers":
    q2point = 1
    q2response = ""
else:
    q2response = "The Pittsburg Steelers with 6 Superbowl wins"
    q2point = 0
if q3=="Drew Brees":
    q3point = 1
    q3response = ""
else:
    q3response = "As of this moment Drew Brees is the NFL leading TD leader "
    q3point = 0
if q4=="Lamar Jackson":
    q4point = 1
    q4response = ""
else:
    q4response = "The 2019 MVP of the NFL was Lamar Jackson"
    q4point = 0
if q5=="Kansas City Chiefs":
    q5point = 1
    q5response = ""
else:
    q5response = "The reigning NFL superbowl champions are the Kansas City Chiefs"
    q5point = 0
#answers
total_points = q1point+q2point+q3point+q4point+q5point
responses = q1response + q2response + q3response + q4response + q5response
#total
if total_points == 5:
    print ("Wow, you are a nfl superfan")
elif total_points == 4:
    print("You got 4/5 correct. You did not know that..",responses)
elif total_points == 3:
    print("You got 3/5 correct. You did not know that..",responses)
elif total_points == 2:
    print("You got 2/5 correct. You did not know that..",responses)
elif total_points == 1:
    print("You got 1/5 correct. You did not know that..",responses)
else:
    print(" You got all answers wrong, time to brush on your nfl knowlegde. You did not know..",responses)




