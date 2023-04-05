WIDTH = 800
HEIGHT = 600
PLAYER_ACC = 0.08
PLAYER_FRICTION = -1
PLAYER_JUMP = 20
PLAYER_GRAV = 0.8
MOB_ACC = 2
MOB_FRICTION = -1
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
GREEN = (0,255,0)
FPS = 60
RUNNING = True
SCORE = 0
PAUSED = False

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, (200,200,200), "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, (100,255,100), "bouncey"),
                 (125, HEIGHT - 350, 100, 5, (200,100,50), "disappearing"),
                 (350, 200, 100, 20, (200,200,200), "normal"),
                 (175, 100, 50, 20, (200,200,200), "normal")]

# wall list
WALL_LIST = [((0, 0, 50, 600, BLACK, "left")), (WIDTH - 50, 0, 50, 600, BLACK, "right")]