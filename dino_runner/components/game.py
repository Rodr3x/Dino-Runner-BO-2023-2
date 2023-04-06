from random import randint
import pygame
from pygame.locals import *
import sys
from dino_runner.components.Dinosaur import Dinosaur
from dino_runner.utils.constants import BG, CLOUD, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, HEART, GAME_OVER, RESET, START, DEFAULT_TYPE
from dino_runner.components import text_utils
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.running = False
        self.playing = False
        self.music_intro = pygame.mixer.music.load("dino_runner/components/music.mp3")
        self.play =  pygame.mixer.music.play(3)
        self.game_speed = 15
        # Para el fondo
        self.x_pos_bg = 0
        self.y_pos_bg = 450
        # Para la nube
        self.x_pos_cloud = SCREEN_WIDTH
        self.y_pos_cloud = 100
        # Para la nube EXTRA
        self.x_pos_cloudE = SCREEN_WIDTH-500
        self.y_pos_cloudE = 85
        # para los corazones
        self.x_pos_heart = SCREEN_WIDTH//2
        self.y_pos_heart = SCREEN_HEIGHT//2
        # lista de puntaje
        self.scores = []
    

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.lifes = 3
        self.points = 0
        self.death_count = 0


    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()

        pygame.time.delay(3000)
        pygame.quit()



    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.quit()

            if event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset()

            pressed_key = pygame.key.get_pressed()
            if pressed_key[K_r] and self.death_count >= 3:  
                self.playing = True
                self.resetTotal()

            if pressed_key[K_q]:  
                self.running = False
                self.playing = False
                pygame.quit()

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(user_input)
            self.obstacle_manager.update(self.game_speed, self.player)
            self.power_up_manager.update(self.game_speed, self.points, self.player)
            self.points += 1
            
            if self.points % 200 == 0:
                self.game_speed += 1

            if self.player.dino_dead:
                self.playing = False
                self.death_count += 1


    def draw(self):
        if self.playing:
            self.clock.tick(FPS)
            self.screen.fill((255, 255, 255))
            self.draw_background()
            self.draw_cloud()
            self.player.draw(self.screen)

            if self.player.time_to_show > 0 and self.player.type != DEFAULT_TYPE:
                self.draw_power(self.player.time_to_show)

            self.draw_score()
            self.draw_life()
            self.obstacle_manager.draw(self.screen)
            self.power_up_manager.draw(self.screen)
            if self.player.dino_dead:
                self.player.drawDead(self.screen)
        else:
            self.draw_menu()

        pygame.display.update()        
        pygame.display.flip()


    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_cloud(self):
        sw = False
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (image_width +self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_width:
            self.screen.blit(CLOUD, (image_width +self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = SCREEN_WIDTH
        self.draw_cloudE()
        self.x_pos_cloud -= self.game_speed

    def draw_cloudE(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (image_width +self.x_pos_cloudE, self.y_pos_cloudE))
        if self.x_pos_cloudE <= -image_width:
            self.screen.blit(CLOUD, (image_width + self.x_pos_cloudE, self.y_pos_cloudE))
            if randint(0, 1) == 0:
                self.x_pos_cloudE = SCREEN_WIDTH
            else:
                self.x_pos_cloudE = randint(2,3)*SCREEN_WIDTH

        self.x_pos_cloudE -= self.game_speed


    def draw_score(self):
        score, score_rect = text_utils.get_message("Points: " + str(self.points), 20, 1000, 40)
        self.screen.blit(score, score_rect)
        
    def draw_life(self):
        lifes, lifes_rect = text_utils.get_message("Lifes: " + str(self.lifes-self.death_count), 20, 1000, 80)
        self.screen.blit(lifes, lifes_rect)
    

    def draw_power(self, c):
        powerH, powerH_rect = text_utils.get_message("PowerUp ({}) ".format((self.player.type).upper()), 20, 150, 40)
        powerT, powerT_rect = text_utils.get_message("Duration: " + str(c) + " sec.", 20, 150, 60)
        self.screen.blit(powerH, powerH_rect)
        self.screen.blit(powerT, powerT_rect)


    def draw_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_element()
    

    def print_menu_element(self):
        if self.death_count == 0:
            self.scores.append(self.points)
            #print(self.scores)
            image_width = HEART.get_width()
            c = -50
            for i in range(3):
                self.screen.blit(HEART, (self.x_pos_heart+c, self.y_pos_heart+100))
                c += 40

            textW, textW_rect = text_utils.get_message("WELCOME TO DINNO RUNNER", 45, SCREEN_WIDTH//2, (SCREEN_HEIGHT//2) - 250)
            self.screen.blit(textW, textW_rect)

            image_width = START.get_width()
            self.screen.blit(START, ((SCREEN_WIDTH//2)-30, (SCREEN_HEIGHT//2)-175))

            text, text_rect = text_utils.get_message("Press any key to start", 30)
            textLives, textLives_rect = text_utils.get_message("You have {} lives".format(3-self.death_count), 25,  height = SCREEN_HEIGHT // 2 + 50)
            self.screen.blit(text, text_rect)
            self.screen.blit(textLives, textLives_rect)
        elif self.death_count < 3:
            self.scores.append(self.points)
            #print(self.scores)
            image_width = HEART.get_width()
            c = -30
            for i in range(3-self.death_count):
                if 3-self.death_count != 1:
                    self.screen.blit(HEART, (self.x_pos_heart+c, self.y_pos_heart+150))
                    c += 40
                else:
                    self.screen.blit(HEART, (self.x_pos_heart-10, self.y_pos_heart+150))
            
            textLives, textLives_rect = text_utils.get_message("You have {} lives".format(self.lifes-self.death_count), 25, height = SCREEN_HEIGHT // 2 + 100)
            text, text_rect = text_utils.get_message("Press any key to restart the game", 30)
            score, score_rect = text_utils.get_message("Your score: "+ str(self.points), 30, height = SCREEN_HEIGHT // 2 + 50)
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
            self.screen.blit(textLives, textLives_rect)

        else:
            self.scores.append(self.points)
            #print(self.scores)

            image_width = GAME_OVER.get_width()
            self.screen.blit(GAME_OVER, (SCREEN_WIDTH//2-200, (SCREEN_HEIGHT//2)-10))

            image_width = RESET.get_width
            self.screen.blit(RESET, (SCREEN_WIDTH//2-35, (SCREEN_HEIGHT//2)+35))
            textA, textA_rect = text_utils.get_message("Press R key to restart lives // Press Q key to quit", 30, SCREEN_WIDTH//2, (SCREEN_HEIGHT//2) + 150)
            self.screen.blit(textA, textA_rect)

            ranking, ranking_rect = text_utils.get_message("RANKING: ", 30, 100, 50)
            self.scores.sort(reverse=True)
            dic = {}
            for i in self.scores:
                dic[i] = dic.get(i, 0) + 1

            esp = 100
            for i in dic.keys():
                if i != 0:
                    score, score_rect = text_utils.get_message("{} points.".format(i), 30, 100, esp)
                    self.screen.blit(score, score_rect)
                    esp += 50
            self.screen.blit(ranking, ranking_rect)


    def reset(self):
        self.game_speed = 15
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0

    def resetTotal(self):
        self.game_speed = 15
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.death_count = 0
        self.lifes = 3
        self.scores = []