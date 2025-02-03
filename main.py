import pygame
import os
import sys
import random


class BlockPuzzle:
    def __init__(self):
        self.board = [[0] * 8 for _ in range(8)]
        self.left = 66
        self.top = 60
        self.cell_size = 30
        self.width = 372
        self.height = 720
        self.now_score = 0
        self.best_score = 0
        self.flag = False
        self.cl = 0
        self.balls = ['0']
        for i in range(1, 7):
            i = str(i)
            fullname = os.path.join('data', f'{i}.png')
            ball = pygame.image.load(fullname)
            self.balls.append(ball)
        self.figuri = []
        for i in range(7, 48):
            i = str(i)
            fullname = os.path.join('data', f'{i}.png')
            ball = pygame.image.load(fullname)
            self.figuri.append(ball)
        self.kod = [[[1, 1]], [[1, 1, 1]], [[4, 4, 4, 4]], [[2, 2, 2, 2, 2]], [[5], [5]], [[6, 6], [6, 6]],
                    [[6, 0], [6, 6]], [[0, 4], [4, 4]], [[0, 3], [3, 0]], [[1, 0], [0, 1]], [[5, 5], [5, 0]],
                    [[1, 1], [0, 1]], [[3, 3, 3], [3, 3, 3]], [[0, 2, 2], [2, 2, 0]], [[0, 1, 0], [1, 1, 1]],
                    [[5, 5, 5], [0, 5, 0]], [[1, 1, 0], [0, 1, 1]], [[6, 6, 6], [6, 0, 0]], [[5, 5, 5], [0, 0, 5]],
                    [[2], [2], [2]], [[4, 4], [4, 4], [4, 4]], [[0, 5], [5, 5], [5, 0]], [[6, 0], [6, 6], [0, 6]],
                    [[3, 0], [3, 3], [3, 0]], [[0, 4], [4, 4], [0, 4]], [[4, 4], [4, 0], [4, 0]],
                    [[3, 3], [0, 3], [0, 3]], [[6, 6, 6], [6, 6, 6], [6, 6, 6]], [[4, 0, 0], [4, 0, 0], [4, 4, 4]],
                    [[0, 0, 1], [0, 0, 1], [1, 1, 1]], [[0, 4, 0], [4, 4, 4], [0, 4, 0]],
                    [[0, 0, 6], [0, 6, 0], [6, 0, 0]], [[3, 0, 0], [0, 3, 0], [0, 0, 3]],
                    [[0, 6, 0], [0, 6, 0], [6, 6, 6]], [[5, 0, 0], [5, 5, 5], [5, 0, 0]],
                    [[0, 0, 2], [2, 2, 2], [0, 0, 2]], [[1, 1, 1], [0, 1, 0], [0, 1, 0]],
                    [[3, 3, 3], [3, 0, 0], [3, 0, 0]], [[5, 5, 5], [0, 0, 5], [0, 0, 5]], [[6], [6], [6], [6]],
                    [[5], [5], [5], [5], [5]]]
        self.reserv = 0
        self.osnov = []
        for i in range(3):
            self.osnov.append(random.randint(7, 47))

    def start(self, b, cl):
        self.cl += cl.tick() / 10
        ing = int(self.cl % 2 + 1)
        fullname = os.path.join('data', f'{ing}.png')
        ball = pygame.image.load(fullname)
        screen.blit(b, (0, 0))
        screen.blit(ball, (230, 247))

    def game(self):
        font = pygame.font.Font(None, 30)
        text = font.render(f'Твой счет: {str(self.now_score)}', True, (0, 255, 0))
        text_x = 50
        text_y = 340
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (255, 255, 255), (35, 400, 100, 100), 1)
        pygame.draw.rect(screen, (255, 255, 255), (141, 400, 100, 100), 1)
        pygame.draw.rect(screen, (255, 255, 255), (246, 400, 100, 100), 1)
        for i in range(8):
            for j in range(8):
                pygame.draw.rect(screen, (255, 255, 255), (
                    j * self.cell_size + self.left, i * self.cell_size + self.top, self.cell_size, self.cell_size), 1)
                if self.board[i][j] != 0:
                    b = self.balls[self.board[i][j]]
                    screen.blit(b, (j * self.cell_size + self.left, i * self.cell_size + self.top))
        if self.osnov[0] != 0:
            b = self.figuri[self.osnov[0] - 7]
            screen.blit(b, (37, 401))
        if self.osnov[1] != 0:
            b = self.figuri[self.osnov[1] - 7]
            screen.blit(b, (143, 401))
        if self.osnov[2] != 0:
            b = self.figuri[self.osnov[2] - 7]
            screen.blit(b, (248, 401))
        if self.reserv != 0:
            b = self.figuri[self.reserv - 7]
            screen.blit(b, (142, 530))

    def on_click(self, cell_coords):
        print(cell_coords)

    def get_cell(self, mouse_pos):
        if 37 < mouse_pos[0] < 137 and 401 < mouse_pos[1] < 501:
            if self.osnov[0] != 0:
                self.flag = True
                self.f = 0
        if 143 < mouse_pos[0] < 243 and 401 < mouse_pos[1] < 501:
            if self.osnov[1] != 0:
                self.flag = True
                self.f = 1
        if 248 < mouse_pos[0] < 348 and 401 < mouse_pos[1] < 501:
            if self.osnov[2] != 0:
                self.flag = True
                self.f = 2
        if 142 < mouse_pos[0] < 242 and 530 < mouse_pos[1] < 630:
            if self.reserv != 0:
                self.flag = True
                self.f = 3
        if self.left <= mouse_pos[1] < self.left + self.height * self.cell_size and self.top <= mouse_pos[0] < self.top + self.width * self.cell_size:
            self.xx, self.yy = (int((mouse_pos[1] - self.left) / self.cell_size), int((mouse_pos[0] - self.top) / self.cell_size))
            if self.xx > 7 or self.xx < 0 or self.yy > 7 or self.yy < 0:
                return None
            else:
                if self.board[self.xx][self.yy] == 0:
                    self.next_hod(self.xx, self.yy)
        else:
            return None

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell != None:
            self.on_click(cell)

    def next_hod(self, x, y):
        temp = []
        if self.flag:
            d = self.kod[22]
            if self.f == 3:
                if self.reserv != 0:
                    d = self.kod[self.reserv - 7]
            else:
                if self.osnov[self.f] != 0:
                    d = self.kod[self.osnov[self.f] - 7]
            f = True
            for i in range(len(d)):
                t = []
                for j in range(len(d[i])):
                    if i + x < 8 and j + y < 8:
                        if d[i][j] + self.board[i + x][j + y] < 1 + max(self.board[i + x][j + y], d[i][j]):
                            t.append(d[i][j] + self.board[i + x][j + y])
                        else:
                            f = False
                            break
                    else:
                        f = False
                        break
                if not f:
                    break
                else:
                    temp.append(t)
            if f:
                if self.f == 3:
                    self.reserv = 0
                else:
                    self.osnov[self.f] = 0
                self.osnov[self.f] = 0
                for i in range(len(temp)):
                    for j in range(len(temp[i])):
                        self.board[i + x][j + y] = temp[i][j]
        fl = False
        for i in range(8):
            k = 0
            for j in range(8):
                if self.board[i][j] != 0:
                    k += 1
            if k == 8:
                for h in range(8):
                    self.board[i][h] = 0
                    fl = True
        if fl:
            self.now_score += 10
        for i in range(8):
            k = 0
            for j in range(8):
                if self.board[j][i] != 0:
                    k += 1
            if k == 8:
                for h in range(8):
                    self.board[h][i] = 0
                    fl = True
        if fl:
            self.now_score += 10
        if self.now_score > self.best_score:
            self.best_score = self.now_score
        if self.osnov[0] == 0 and self.osnov[1] == 0 and self.osnov[2] == 0:
            self.next_lvl()

    def next_lvl(self):
        self.osnov = []
        for i in range(3):
            self.osnov.append(random.randint(7, 48))


pygame.init()
screen = pygame.display.set_mode((372, 720))
fullname = os.path.join('data', 'start.jpg')
clock = pygame.time.Clock()
pygame.display.set_caption('Block Puzzle')
s = 0
ing = 0
if not os.path.isfile(fullname):
    sys.exit()
ball = pygame.image.load(fullname)
running = True
board = BlockPuzzle()
cl = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if s == 0:
                s = 1
            else:
                board.get_click(event.pos)
    if s == 0:
        board.start(ball, cl)
    else:
        screen.fill((0, 0, 0))
        board.game()
    pygame.display.flip()
    clock.tick(50)
pygame.quit()