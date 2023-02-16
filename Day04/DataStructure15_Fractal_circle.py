#프랙탈 원 그리기
import turtle
t=turtle.Turtle()


c=t.clone()
c.shape('turtle')
c.color=('red')
c.circle(30)
c.speed(3)


for i in range(4,10):
    c.circle(i*10)

turtle.mainloop()