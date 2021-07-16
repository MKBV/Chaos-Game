import turtle, random, math

s = turtle.getscreen()
s.bgcolor("#16161d")
t = turtle.Turtle(visible=False)
t.pencolor("white")
t.pensize(3)
t.speed(5)

##Corners & Borders
c1 = 300,300		#Changeable as c1 = x , y
c2 = -300,300		#
c3 = -300,-300		#
c4 = 300, -300		#

crn = [c1,c2,c3,c4]
chk = [[c1[0],c2[0],c3[0],c4[0]],[c1[1],c2[1],c3[1],c4[1]]]
bminx = min(chk[0])
bmaxx = max(chk[0])
bminy = min(chk[1])
bmaxy = max(chk[1])

##Draw triangle
t.penup()
t.goto(c4[0],c4[1])
t.pendown()

for drwcrn in crn:
	t.goto(drwcrn[0],drwcrn[1])

##First Dot
t.speed(100)
t.pensize(1)
t.penup()
while True:
	xd = random.uniform(bminx, bmaxx)
	yd = random.uniform(bminy, bmaxy)

	def area(a,b,c,d,e,f):
		return abs(a*d+c*f+e*b-c*b-e*d-a*f)/2

	at1 = area(c1[0],c1[1],c2[0],c2[1],c3[0],c3[1])
	at2 = area(c1[0],c1[1],c4[0],c4[1],c3[0],c3[1])
	a1 = area(c1[0],c1[1],c2[0],c2[1],xd,yd)
	a2 = area(c1[0],c1[1],c4[0],c4[1],xd,yd)
	a3 = area(c2[0],c2[1],c3[0],c3[1],xd,yd)
	a4 = area(c4[0],c4[1],c3[0],c3[1],xd,yd)

	if a1+a2+a3+a4==at1+at2:
		break
t.goto(xd,yd)
t.dot("red")

##Dots
shcd = 0 		#for change the shape 0, 1, 2
chk = []
t.pensize(0.1)
while True:
	rcr = random.choice(crn)
	if rcr != chk:
		xt = (rcr[0]+t.pos()[0])/2
		yt = (rcr[1]+t.pos()[1])/2
		t.goto(xt,yt)
		t.dot("#00ff00")
		chk = crn[(crn.index(rcr)+shcd)%4]
