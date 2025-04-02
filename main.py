import pygame,random
pygame.init()

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
yellow = (0,255,255)


screen_width = 800
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width , screen_height)) #Takes value in tuple
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
fps = 30
font = pygame.font.SysFont(None, 50)

with open('highscore.txt' , 'r') as file:
    highscore = file.read()

def snake_body(screen, color, snake_position, size) :
    for x , y in snake_position :
        pygame.draw.rect(screen, color, [x , y ,size , size])

def text_screen(text , color , x , y) :
    screen_text = font.render(text, True , color)
    gameWindow.blit(screen_text , [x,y])

def generate_food(snake_position):
    while True:
        food_x = random.randint(200, screen_width - 200)
        food_y = random.randint(150, screen_height - 150)
        if [food_x, food_y] not in snake_position:
            return food_x, food_y
def home_page():
    gameWindow.fill(white)
    exit_game = False
    while not exit_game :
        text_screen('Snake Game', black, 280, 100)
        text_screen('Press space to play', black, 250, 200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    game_loop()
        clock.tick(fps)
        pygame.display.update()

def game_loop():
    global highscore
    exit_game = False
    game_over = False
    snake_x = 100
    snake_y = 250
    snake_size = 15
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(200, screen_width - 200)
    food_y = random.randint(150, screen_height - 150)
    food_size = 10
    snake_position = []
    snake_length = 1
    score = 0
    while not exit_game :
        if game_over :
            gameWindow.fill(white)
            text_screen(f'Score : {score}', green, 100, 100)
            text_screen(f'Highscore : {highscore}', black, 100, 200)
            text_screen('Please press enter to restart', red , 100 , 300)
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN :
                        game_loop()
                # if event.type == pygame.MOUSEMOTION :
                #     x , y = event.pos
                #     if x == 100 and y == 300 :
                #         game_loop()

        else :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT :
                        velocity_x = 6
                        velocity_y = 0
                    if event.key == pygame.K_LEFT :
                        velocity_x = -6
                        velocity_y = 0
                    if event.key == pygame.K_UP :
                        velocity_y = -6
                        velocity_x = 0
                    if event.key == pygame.K_DOWN :
                        velocity_y = 6
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x)<10 and  abs(snake_y - food_y)<10 :
                score += 1
                food_x, food_y = generate_food(snake_position)
                snake_length += 3
                if score>int(highscore) :
                    highscore = score
                    with open('highscore.txt' , 'w') as f:
                        f.write(str(highscore))

            gameWindow.fill(white)
            text_screen(f'Score : {score}', green, 5, 5)
            pygame.draw.rect(gameWindow , red , [food_x, food_y , food_size , food_size])

            head = [snake_x, snake_y]
            snake_position.append(head)
            if len(snake_position)>snake_length :
                del snake_position[0]

            if head in snake_position[:-1] :
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height :
                game_over = True

            snake_body(gameWindow , black , snake_position , snake_size)
        clock.tick(fps)
        pygame.display.update()

    pygame.quit()
    quit()
home_page()