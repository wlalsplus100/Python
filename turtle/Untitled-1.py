'''
키보드 입력에 따라 거북이가 움직이며
그림도 그릴 수 있는 파이썬 프로그램입니다.
by 탐구소년
'''
import turtle

# 각종 설정
player = turtle.Turtle()
player.color("#FFBB00") #색깔 정하기 with RGB code
player.shape("turtle") #모양 정하기
player.speed(0) #속도는 숫자가 작을수록 빠름
screen = player.getscreen()
player.penup() # 펜 들기 == 그림 그리지 않는 상태

# left, right 는 각도 변경
def left() :
    player.left(40)
def right():
    player.right(40)

# forward, backward 는 거리 이동
def up() :
    player.forward(30)
def down() :
    player.backward(30)

# circle 은 원의 크기
def circle() :
    player.circle(30)

# 최근동작 취소 (ctrl+z와 같은 동작)
def undo() :
    player.undo()

# 그림 그리기 여부 변경
def space() :
    if player.isdown() :
        player.penup()
    else :
        player.pendown()

# 프로그램(창) 끈다
def endProgram() :
    screen.bye()

# onkeypress(함수명, 키보드버튼명) :
# 어떤 버튼을 눌렀을 때, 이 함수가 동작하도록 하겠다!
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(circle, "o")
screen.onkeypress(undo, "z")
screen.onkeypress(space, "space")
screen.onkeypress(endProgram, "q")
screen.listen() # 프로그램 활성화
screen.mainloop() # 프로그램이 계속 동작하는 상태를 유지하겠다!