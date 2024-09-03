from turtle import forward, backward, left, pen, right, mainloop, begin_fill, end_fill, circle, fillcolor, goto, dot, penup, pendown, speed, write

speed(50)
fillcolor('gold')
begin_fill()
#kepala
penup()
goto(0, 170)
pendown()
backward(15)
left(30)
backward(10)
right(120)
backward(7)
right(30)
forward(10)
right(120)
forward(10)
left(150)
forward(10)
right(120)
forward(10)
left(150)
forward(10)
right(120)
forward(12)
left(150)
forward(15)
right(165)
circle(15, 110)
left(120)
circle(-20, 70)
right(100)
circle(-17, 50)
left(150)
circle(20, 70)
circle(-10, 150)
forward(58)
right(-115)
forward(88)
left(115)
forward(58)
circle(-10, 20)
forward(30)
circle(10, 40)
right(315)
backward(10)
right(20)
forward(15)
right(150)
forward(15)
left(150)
forward(5)
circle(10, 60)
right(150)
circle(10, 60)
left(60)
circle(10, 60)
right(76)
forward(12)
end_fill()
#perisai
penup()
goto(-65, 64)
pendown()
left(6)
backward(150)
left(90)
forward(100)
circle(-72, 90)
right(3)
circle(-75, 90)
left(5)
forward(94)
#p.merah 1
fillcolor('red')
begin_fill()
penup()
goto(13, 64)
pendown()
right(2)
backward(75)
left(90)
forward(71)
end_fill()
#p.merah 2
fillcolor('red')
begin_fill()
penup()
goto(14, 68)
pendown()
right(90)
backward(175)
right(90)
circle(72, 90)
forward(30)
left(90)
forward(66)
end_fill()
#p.hitam
fillcolor('black')
begin_fill()
penup()
goto(-15,10)
pendown()
backward(50)
left(90)
forward(40)
circle(-25,90)
right(3)
circle(-25,90)
left(5)
forward(40)
end_fill()
#sayap kiri
fillcolor('gold')
begin_fill()
penup()
goto(50,80)
pendown()
left(90)
circle(-45,-70)
circle(10,-70)
circle(-90,-110)
right(-45)
circle(-150,110)
forward(130)
circle(-30,60)
forward(57)
right(140)
circle(45,65)
right(3)
forward(113)
left(90)
forward(27)
right(62)
forward(16)
end_fill()
#sayap kanan
fillcolor('gold')
begin_fill()
penup()
goto(-30,80)
pendown()
left(-115)
circle(45,-70)
circle(-10,-70)
circle(90,-110)
right(45)
circle(150,110)
forward(130)
circle(25,60)
forward(57)
right(-140)
circle(-35,65)
forward(120)
left(-90)
forward(26)
right(-62)
forward(16)
end_fill()

#ekor
fillcolor('gold')
begin_fill()
penup()
goto(-5,-105)
pendown()
right(5)
backward(150)
right(90)
circle(30,90)
left(30)
backward(30)
right(90)
circle(20,95)
backward(32)
right(90)
circle(20,95)
backward(33)
right(90)
circle(20,95)
right(30)
circle(-20,-95)
right(90)
forward(33)
circle(-20,-95)
right(90)
forward(32)
circle(-20,-95)
right(90)
forward(30)
left(30)
circle(-30,-95)
right(90)
forward(157)
right(103)
circle(57,-45)
end_fill()

#pita cengkraman
fillcolor('white')
begin_fill()
penup()
goto(-105,-145)
pendown()   
circle(300,50)
right(90)
forward(25)
right(90)
circle(-330,50)
right(90)
forward(27)
end_fill()

#kaki kanan
fillcolor('gold')
begin_fill()
penup()
goto(65,-85)
pendown()
left(60)
backward(75)
circle(70,-30)
left(90)
forward(15)
left(90)
circle(-50,-30)
right(90)
forward(15)
left(-150)
forward(20)
right(120)
backward(25)
left(30)
backward(47)
left(60)
forward(45)
end_fill()

#kaki kiri
fillcolor('gold')
begin_fill()
penup()
goto(-45,-83)
left(25)
pendown()
backward(75)
circle(-70,-30)
left(-105)
forward(15)
left(-80)
circle(50,-30)
right(-90)
forward(15)
left(150)
forward(20)
right(-123)
backward(25)
left(-30)
backward(53)
left(-60)
forward(45)
end_fill()

#mata
fillcolor('white')
begin_fill()
penup()
goto(-20,155)
pendown()
right(60)
circle(-7,-180)
right(90)
forward(14)
end_fill()

penup()
goto(-15,152)
dot(7)

#ujung kiri
penup()
goto(-105,-172)
pendown()
left(60)
forward(20)
right(150)
forward(20)

penup()
goto(-115,-190)
pendown()
left(70)
forward(70)
right(160)
forward(30)
left(150)
forward(30)
right(160)
forward(63)

#ujung kanan
penup()
goto(155,-167)
pendown()
left(-60)
forward(20)
right(150)
forward(23)

penup()
goto(162,-187)
pendown()
left(-110)
forward(70)
right(-160)
forward(30)
left(-150)
forward(30)
right(-160)
forward(63)

#tulisan Bhineka Tunggal Ika
penup()
goto(-45,-160)
pendown()
write('BHINEKA TUNGGAL IKA', align='center', font='Times New Roman')

mainloop()