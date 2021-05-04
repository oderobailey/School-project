print("Hello and wlecome to a quiz all about me ")
#hello world
q1 = input("Question 1: Where was I born?")
q2 = input("Question 2: How old am I?")
q3 = input("Question 3: What my favorite animal?")
q4 = input("Question 4: What college do I currently attend?")
#question
if q1=="Jamaica":
    q1point = 1
    q1response = ""
else:
    q1response = "I am from Jamaica"
    q1point = 0
if q2=="21":
    q2point = 1
    q2response = ""
else:
    q2response = "I am 21 years old"
    q2point = 0
if q3=="wolf":
    q3point = 1
    q3response = ""
else:
    q3response = "My favorite animal is a wolf"
    q3point = 0
if q4=="Suny Albany":
    q4point = 1
    q4response = ""
else:
    q4response = "I attending Suny Albany"
    q4point = 0
#answers
total_points = q1point+q2point+q3point+q4point
responses = q1response+q2response+q3response+q4response
#total
if total_points == 4:
    print ("Wow, you know alot about me")
elif total_points == 3:
    print("You got 3/4 correct. You did not know that..",responses)
elif total_points == 2:
    print("You got 2/4 correct. You did not know that..",responses)
elif total_points == 1:
    print("You got 1/4 correct. You did not know that..",responses)
else:
    print(" You got all answers wrong. You did not know..",responses)





