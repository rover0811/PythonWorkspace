import pygame,sys
from pygame.locals import*
from rule import*

board_color1 = (153, 102, 000)
board_color2 = (153, 102, 51)
board_color3 = (204, 153, 000)
board_color4 = (204, 153, 51)
bg_color = (128, 128, 128)
black = (0, 0, 0)
blue = (0, 50, 255)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)

window_width = 800
window_height = 500
board_width = 500
board_size = 15
grid_size = 30
empty = 0
black_stone = 1
white_stone = 2
tie = 100

fps = 60
fps_clock = pygame.time.Clock()

def main():
    pygame.init()
    surface = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Omok game")
    surface.fill(bg_color)                      #여기까지 필수 항목

    omok = Omok(surface)
    menu = Menu(surface)
    while True:                                 #게임이 끝나도 프로그램이 종료함을 막기 위함
        run_game(surface, omok, menu)
        menu.is_continue(omok)
        
def run_game(surface, omok, menu):
    omok.init_game()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                menu.terminate()
            elif event.type == MOUSEBUTTONUP:
                if not omok.check_board(event.pos):
                    if menu.check_rect(event.pos, omok):
                        omok.init_game()

        if omok.is_gameover:
            return

        pygame.display.update()
        fps_clock.tick(fps)


