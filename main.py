import pygame
import sys
import random

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))

class Player:
    def __init__(self):
        self.hp = 100
        self.player_x = 0
        self.player_y = screen_height // 2
        self.player_a = screen_height // 15
        self.points = 0

    def move(self, direction):
        if direction == "up" and self.player_y > 70:
            self.player_y -= 10
        elif direction == "down" and self.player_y < screen_height - self.player_a:
            self.player_y += 10
        elif direction == "right" and self.player_x < 200:
            self.player_x += 10
        elif direction == "left" and self.player_x > 0:
            self.player_x -= 10

    def draw(self):
        player_rect = pygame.Rect(self.player_x, self.player_y, self.player_a, self.player_a)
        pygame.draw.rect(screen, (255, 255, 255), player_rect)
        return player_rect

    def display_statistics(self):
        font = pygame.font.Font(None, 36)
        text = f"HP: {self.hp}, coordinates: X: {self.player_x}, Y: {self.player_y} Points: {self.points}"
        text_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, (330, 20))

    def collide(self, obj, obj2, obj3, obj4):
        player_rect = self.draw()
        if player_rect.colliderect(obj.draw()) and obj.ob:
            self.hp -= 10
            obj.visible = False
        elif player_rect.colliderect(obj2.draw()) and obj.ob2:
            self.hp -= 10
            obj2.visible = False
        elif player_rect.colliderect(obj3.draw()) and obj.ob3:
            self.hp -= 10
            obj3.visible = False
        elif player_rect.colliderect(obj4.draw()) and obj.ob4:
            self.hp -= 10
            obj4.visible = False

player = Player()

class Obj:
    def __init__(self):
        self.hp = 20
        self.speed = 10
        self.obj_x = 950
        self.obj_y = 70
        self.obj_a = 50
        self.visible = True
        self.ob = True
        self.ob2 = False
        self.ob3 = False
        self.ob4 = False
        self.ob5 = False

    def move(self):
        if self.obj_x > 1:
            movement_speed = self.speed + random.randint(1, 20)
            self.obj_x -= movement_speed
        else:
            self.visible = False

    def draw(self):
        obj_rect = pygame.Rect(self.obj_x, self.obj_y, self.obj_a, self.obj_a)
        pygame.draw.rect(screen, (255, 0, 0), obj_rect)
        return obj_rect

obj = Obj()
obj2 = Obj()
obj3 = Obj()
obj4 = Obj()
obj5 = Obj()

class Interface:
    def __init__(self):
        self.color = "white"

    def draw(self):
        black_rect = pygame.Rect(950, 70, 50, 50)
        pygame.draw.rect(screen, "black", black_rect)
        pygame.draw.line(screen, self.color, (0, 70), (1000, 70))
        pygame.draw.line(screen, self.color, (200 + screen_height // 15, 70), (200 + screen_height // 15, 1000))

    def defeat(self):
        font = pygame.font.Font(None, 200)
        text = "DEFEAT"
        text_surface = font.render(text, True, (255, 0, 0))
        screen.blit(text_surface, (300, 350))

interface = Interface()

clock = pygame.time.Clock()
fps = 60

game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player.move("up")
    if keys[pygame.K_DOWN]:
        player.move("down")
    if keys[pygame.K_LEFT]:
        player.move("left")
    if keys[pygame.K_RIGHT]:
        player.move("right")

    screen.fill((0, 0, 0))
    player.display_statistics()
    player.collide(obj, obj2, obj3, obj4)

#OBJ 1
    if player.points == 0:
        obj.ob = True
        obj.draw()
    if obj.visible == True and obj.ob == True:
        obj.move()
    elif obj.visible == False  and obj.ob == True:
        obj.obj_x = 950
        obj.obj_y = random.randint(70, 950)
        player.points += 1
        obj.visible = True
    player.draw()
# OBJ 2
    if player.points > 15:
        obj.ob2 = True

    if obj2.visible == True and obj.ob2 == True:
        obj2.move()
    elif obj2.visible == False and obj.ob2 == True:
        obj2.visible = True
        obj2.obj_x = 950
        obj2.obj_y = random.randint(70, 950)
        player.points += 1
    obj2.draw()

# OBJ 3
    if player.points > 45:
        obj.ob3 = True

    if obj3.visible == True and obj.ob3 == True:
        obj3.move()
    elif obj3.visible == False and obj.ob3 == True:
        obj3.visible = True
        obj3.obj_x = 950
        obj3.obj_y = random.randint(70, 950)
        player.points += 1
    obj3.draw()

# OBJ 4
    if player.points > 150:
        obj.ob4 = True


    if obj4.visible == True and obj.ob4 == True:
        obj4.move()
    elif obj4.visible == False and obj.ob4 == True:
        obj4.visible = True
        obj4.obj_x = 950
        obj4.obj_y = random.randint(70, 950)
        player.points += 1
    obj4.draw()
    
# OBJ 5
    if player.points > 500:
        obj.ob5 = True


    if obj5.visible == True and obj.ob5 == True:
        obj5.move()
    elif obj5.visible == False and obj.ob5 == True:
        obj5.visible = True
        obj5.obj_x = 950
        obj5.obj_y = random.randint(70, 950)
        player.points += 1
    obj5.draw()

    interface.draw()
    
    if player.hp <= 0:
        interface.defeat()
        game_over = True
        
    pygame.display.flip()
    pygame.display.update()
    clock.tick(fps)

    if game_over == True:
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

