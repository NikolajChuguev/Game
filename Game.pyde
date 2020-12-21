x=500
y=500
x1=x/2
y1=1000
speed=20
dim=100
dy=20
dx=10
score = 0

def setup() :
    size(x*3, y*2)
    fill(0)

def keyPressed():
    global x1,y1
    if key == 'a':
        x1 = x1-speed
    if key == 'd':
        x1 = x1+speed
    if x1 > width:
      x1 = 0
    if x1 < -100:
      x1 = width-100
    
def draw():
    global x1,y1, score 
    background(0, 204, 102)
    stroke(0, 153, 51)
    fill(0, 0, 204)
    rect(x1,0,200,50)
    fill(255, 0, 0)
    rect(x1,y1/1.05,200,50)
    if y >= height - 80 or y <= 80:
        if x >= x1 and x <= x1 + 200:
            fill(255, 255, 0)
            text("+1", width/2 + 250, height/2)
            textSize(80)
            score = score + 1
        else:
            score = 0
    fill(255, 255, 0)
    text(int(score), width/2 + 150, height/2)
    text("Score : ", width/2 - 150, height/2)
    frameRate(30)
    global x, y, dy, dx
    y = y + dy
    x = x + dx
    dy=dy
    if y >= height or y <= 0:
        dy = -1*dy
    else:
        translate(x,y)
        fill(255, 255, 255)
        ellipse(0,0, dim/2, dim/2)
        stroke(255,0,0)
    if x > width-dim/4 or x<dim/4:
        dx = -1*dx
    if x >= x1 and x <= x1 + 200 :
        if y >= height - 80 or y <= 80:
            dy = -1*dy
    

    





            
