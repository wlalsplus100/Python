import pygame
import random
import time

pygame.init() #초기화

#화면 크기 설정
screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))

#창 이름 설정
pygame.display.set_caption("Example")

# FPS설정 
clock = pygame.time.Clock()

s_font = pygame.font.SysFont("arial", 15, True, True)
m_font = pygame.font.SysFont("arial", 30, True, True)
l_font = pygame.font.SysFont("arial", 45, True, True)

#배경이미지 설정
background = pygame.image.load(".\\pygame\\resource\\rose.jpg")
background = pygame.transform.scale(background, (640, 480))

#캐릭터 불러오기
character = pygame.image.load(".\\pygame\\resource\\찬희얼굴딱맞춤.png")
character = pygame.transform.scale(character, (100, 100))
character_size = character.get_rect().size # 캐릭터의 사이즈 가져오기
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_position = (screen_width / 2) - (character_width / 2) # 화면 가로에 중간지점에 캐릭터의 가로 위치
character_y_position = screen_height - character_height # 화면 세로 크기 가장 아래에 캐릭터의 세로 위치

enemy = pygame.image.load(".\\pygame\\resource\\bat.jpg") 
enemy = pygame.transform.scale(enemy, (50, 50)) 
enemy_size = enemy.get_rect().size 
enemy_width = enemy_size[0] 
enemy_height = enemy_size[1] 
enemy_x_position = (screen_width / 2) - (character_width / 2) 
enemy_y_position = 0 

# 이동할 좌표
to_x = 0
to_y = 0

enemy_x = random.randint(-5, 5)
enemy_y = random.randint(-5, 5)
# 이동 속도
character_speed = 0.5
enemy_speed = 0.0005

# 게임 타이머
st = time.time()

#pygame에서는 이벤트 루프가 있어야 창이 꺼지지않음
# 이벤트 루프
running = True # 게임이 진행중인지 확인하기
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수 설정
    nt = time.time() # 게임이 실행되고 진행된 현재 시간(초)

    if int(nt - st) % 10 == 1: 
        enemy_speed += 0.0005 
    
    time_text = s_font.render("TIME : " + str(int(nt - st)), True, (0, 0, 0))

    #fps = ("fps : " + str(clock.get_fps())) #프레임 수 확인
    fps = clock.get_fps() #프레임 수 확인
    text = s_font.render("FPS : " + str(int(fps)), True, (0, 0, 0))

    for event in pygame.event.get(): # running 중 키보드나,마우스 입력값(이벤트)을 체크해주는것
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는지
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed # -5만큼
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= character_speed
            elif event.key -- pygame.K_DOWN: # 캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0


    screen.fill((0, 0, 255)) #RGB형식으로 이미지 로드
    screen.blit(background, (0, 0)) # 배경 그리기(background 가 표시되는 위치)

    screen.blit(character, (character_x_position, character_y_position)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_position, enemy_y_position))
    screen.blit(text, (0, 0))
    screen.blit(time_text, (screen_width - time_text.get_rect().size[0], 0))

    character_x_position += to_x * dt # 캐릭터의 포지션을 x만큼 실제 움직임 프레임수(dt)만큼 곱해서
    character_y_position += to_y * dt # 캐릭터의 포지션을 x만큼 실제 움직임

    enemy_x_position += enemy_x * dt * enemy_speed 
    enemy_y_position += enemy_y * dt * enemy_speed 



    # X 경계값 설정
    if character_x_position < 0:
        character_x_position = 0 
    elif character_x_position > screen_width - character_width:
        character_x_position = screen_width - character_width
    # Y 경계값 설정
    if character_y_position < 0 :
        character_y_position = 0
    elif character_y_position > screen_height - character_height:
        character_y_position = screen_height - character_height

    # 적이 벽에 닿을 경우 방향 재설정
    if enemy_x_position < 0: 
        enemy_x = random.randint(1, 5)
        enemy_y = random.randint(-5, 5)
    elif enemy_x_position > screen_width - enemy_width:
        enemy_x = random.randint(-5, 1)
        enemy_y = random.randint(-5, 5)
    if enemy_y_position < 0:
        enemy_x = random.randint(-5, 5)
        enemy_y = random.randint(1, 5)
    elif enemy_y_position > screen_height - enemy_height:
        enemy_x = random.randint(-5, 5)
        enemy_y = random.randint(-5, 1)
    if enemy_x == 0 and enemy_y == 0:
        while enemy_x != 0 or enemy_y != 0:
            enemy_x = random.randint(-5, 5)
            enemy_y = random.randint(-5, 5)

    character_rect = character.get_rect()
    character_rect.top = character_x_position
    character_rect.left = character_y_position
    enemy_rect = enemy.get_rect()
    enemy_rect.top = enemy_x_position
    enemy_rect.left = enemy_y_position

    if character_rect.colliderect(enemy_rect):
        if enemy_x_position < character_x_position + character_width and enemy_x_position > character_x_position:
            enemy_x_position = character_x_position + character_width 
            print("오른쪽 충돌")
            enemy_x = random.randint(1, 5)
            enemy_y = random.randint(-5, 5)
        elif enemy_x_position > character_x_position - enemy_width:
            enemy_x_position = character_x_position - enemy_width
            print("왼쪽 충돌")
            enemy_x = random.randint(-5, -1)
            enemy_y = random.randint(-5, 5)
        if enemy_y_position > character_y_position - enemy_height and enemy_y_position < character_y_position:
            enemy_y_position = character_y_position - enemy_height
            print("위쪽 충돌")
            enemy_x = random.randint(-5, 5)
            enemy_y = random.randint(-5, -1)
        elif enemy_y_position > character_y_position + enemy_height and enemy_y_position > character_y_position:
            enemy_y_position = character_y_position + character_height
            print("아래쪽 충돌")
            enemy_x = random.randint(-5, 5)
            enemy_y = random.randint(1, 5)
        if enemy_x == 0 and enemy_y == 0:
            while enemy_x != 0 or enemy_y != 0:
                enemy_x = random.randint(-5, 5)
                enemy_y = random.randint(-5, 5)


        

    pygame.display.update() # 게임화면을 지속적으로 그리기(for 문도는동안 계속)

# pygame 종료
pygame.quit()
