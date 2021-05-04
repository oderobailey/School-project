from graphics import*
import random
from datetime import*
#new window
myWindow = GraphWin('Please take my reflex test',500,600)
start = datetime.utcnow()
rx=[]
ry=[]
i=2
while i>0:
    rx.append(random.randint(1,500))
    ry.append(random.randint(75,500))
    i=i-1
#create rectangle
rx.sort()
ry.sort()
rec = Rectangle(Point(rx[0],ry[0]),Point(rx[1],ry[1]))
#add color
rec.setFill("red")
rec.draw(win)
#add user click
testClick = win.getMouse()
end=datetime.utcnow()
xClick = testClick.x
yClick = testClick.y
#inside box
if xClick>rx[0] and xClick<rx[1] and yClick>ry[0] and yClick<ry[1]:
    reflex = end-start
    refPrint = str(reflex)
    msg3 = Text(Point(250,550),"It took this long to click the box:"+ refPrint)
    msg3.draw(win)
else:
    msg3 = Text(Point(250,550),"You did not click in the box")
    msg3.draw(win)

