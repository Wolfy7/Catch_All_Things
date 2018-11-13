
import pygame
from random import randrange, choice, randint
from enum import Enum
import os

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
GRAY = (120,120,120)

GAME_WIDTH = 800
GAME_HEIGHT = 600

things_imgs = [] #TODO

class GameState(Enum):
	TITLE = 1
	RUN = 2
	GAMEOVER = 3
	EXIT = 4
	
class Cat(object):
	def __init__(self):
		self.x = 382
		self.y = 4
		
		c = randint(1,5) 
		#c = 5
		
		if( c == 1):
			self.img = pygame.image.load("assets/cat_red.png")
			self.type = "red"
			self.specialReady = False
			self.specialTime = 0
		elif(c == 2):
			self.img = pygame.image.load("assets/cat_black.png")
			self.type = "black"
			self.specialReady = False
			self.specialTime = 0
		elif(c == 3):
			self.img = pygame.image.load("assets/cat_blue.png")
			self.type = "blue"
			self.specialReady = False
			self.specialTime = 0
		elif(c == 4):
			self.img = pygame.image.load("assets/cat_green.png")
			self.type = "green"
			self.specialReady = False
			self.specialTime = 0
		elif(c == 5):
			self.img = pygame.image.load("assets/cat_pink.png")
			self.type = "pink"
			self.specialReady = False
			self.specialTime = 0
		
	
class Powerup(object):
	def __init__(self):
		self.x = randrange(0, GAME_WIDTH-48) #TODO: replace 10 with Thing width
		self.y = randrange(-600, -200, 10)
		self.speed = 4 
		
		t = randint(1,3) 
		
		if( t == 1):
			self.img = pygame.image.load("assets/live.png")
			self.type = "live"
		elif(t == 2):
			self.img = pygame.image.load("assets/star.png")
			self.type = "star"
		elif(t == 3):
			self.img = pygame.image.load("assets/clock_slow.png")
			self.type = "slow"
		
		self.hitbox_x = self.x
		self.hitbox_y = self.y
		self.hitbox_width = 48
		self.hitbox_height = 48
	

class Thing(object):
	def __init__(self):
		self.x = randrange(0, GAME_WIDTH-48) #TODO: replace 10 with Thing width
		self.y = randrange(-400, -200, 10)
		#print(self.y)
		self.speed = 4 
		self.speedX = choice([-5, 5])  
		self.img = choice(things_imgs)
		
		self.hitbox_x = self.x
		self.hitbox_y = self.y
		self.hitbox_width = 48
		self.hitbox_height = 48
		
class Hand(object):
	def __init__(self):
		self.x = GAME_WIDTH/2
		self.y = GAME_HEIGHT - 130
		self.x_change = 0
		self.speed = 6
		#self.img = pygame.image.load("assets/hand.png")
		self.img = pygame.image.load(choice(("assets/rock_hand.png", "assets/hand.png")))
		
		
		self.hitbox_x = self.x + 9
		self.hitbox_y = self.y + 5
		self.hitbox_width = 112
		self.hitbox_height = 48



def main():
	pygame.mixer.init(22050, -16, 2, 4096)
	pygame.mixer.init()
	pygame.init()
	pygame.mixer.music.load("sounds/BeepBox-Song.wav")	
	screen = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT)) #pygame.FULLSCREEN)
	pygame.display.set_caption("Catch All Things - GPPCC11")
	
	clock = pygame.time.Clock()
	
	h1 = pygame.font.SysFont("comicsansms", 50)
	h2 = pygame.font.SysFont("comicsansms", 36)
	h3 = pygame.font.SysFont("comicsansms", 30)
	h4 = pygame.font.SysFont("comicsansms", 22)
	
	gs = GameState.TITLE
	count = 0
	
	while gs != GameState.EXIT:
		
		print()
		
		title = pygame.image.load("assets/title2.png")
	
		# Title Screen
		while gs == GameState.TITLE:
			screen.fill(BLACK)
			
			screen.blit(title, [0,0])	
		
			start_text = "- PRESS ENTER TO START -"
			screen_text = h1.render(start_text, True, WHITE)
			t_size  = h1.size(start_text)
			
			count += 1
			if count % 2 == 0:
				screen.blit(screen_text, [(GAME_WIDTH/2)-t_size[0]/2,(GAME_HEIGHT-50)-t_size[1]/2])	
			
			for event in pygame.event.get():
				#print(event)
				if event.type == pygame.QUIT:
					gs = GameState.EXIT
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
						gs = GameState.RUN	
						pygame.mixer.music.play(-1)				
			
			pygame.display.flip()
			clock.tick(2)
		
		player = Hand()
		cat = Cat()
		things = []
		powerups = []
		del things_imgs[:]
		lives = 3
		level = randint(1,2)#1
		
		explosion = pygame.mixer.Sound("sounds/Explosion.wav")
		catch = pygame.mixer.Sound("sounds/Catch.wav")
		powerup = pygame.mixer.Sound("sounds/Powerup.wav")		
		miau = pygame.mixer.Sound("sounds/miau.wav")
	
		live = pygame.image.load("assets/live_trans.png")
		time = pygame.image.load("assets/clock_trans.png")
		star = pygame.image.load("assets/star_bw_trans.png")
		frame = pygame.image.load("assets/frame_trans.png")
		
		if level == 1:			
			bg = pygame.image.load("assets/room_lr.png")
			things_imgs.append(pygame.image.load("assets/beer.png"))
			things_imgs.append(pygame.image.load("assets/beer2.png"))
			things_imgs.append(pygame.image.load("assets/pizza.png"))
		elif level == 2:
			bg = pygame.image.load("assets/room_k.png")
			things_imgs.append(pygame.image.load("assets/cup.png"))
			things_imgs.append(pygame.image.load("assets/frootloops.png"))		
			things_imgs.append(pygame.image.load("assets/coffee_machine.png"))

		pygame.time.set_timer(pygame.USEREVENT + 1, 1000) # Used to correctly implement seconds
		sec = 0
		score = 0
		star_time = 0
		slow_time = 0
		
		# Game loop
		while gs == GameState.RUN:

			clock.tick(60)
			
			for event in pygame.event.get():
				#print(event)
				if event.type == pygame.QUIT:
					gs = GameState.EXIT
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:						
						if(cat.type == 'blue' and cat.specialTime > 0): #TODO
							cat.specialTime -= 1
							player.x_change = player.speed
						else:
							player.x_change = -player.speed
					if event.key == pygame.K_RIGHT:
						if(cat.type == 'blue' and cat.specialTime > 0): #TODO
							cat.specialTime -= 1
							player.x_change = -player.speed
						else:
							player.x_change = player.speed
			
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
						player.x_change = 0
	
				if event.type == pygame.USEREVENT + 1:
					#if (sec % 2) == 0:
					things.append(Thing())
					if(randint(1,10) == 1):
						powerups.append(Powerup())
						
					if(cat.type == 'red' and cat.specialTime > 0): #TODO
						cat.specialTime -= 10
						things.append(Thing())					
						
					if(cat.specialReady):
						cat.specialTime = 50
						cat.specialReady = False
						
					if(randint(1,20) == 1):
						print("CAT %s SPECIAL !!!" %cat.type) #TODO
						miau.play()
						cat.specialReady = True	
						
					#print("star time:", star_time)
					if star_time > 0:
						star_time -= 1
						
					#print("slow time:", slow_time)
					if slow_time > 0:
						slow_time -= 1
					sec += 1
					#print(sec)
							
			player.x += player.x_change
			player.hitbox_x += player.x_change
			
			#print(player.x)
			if player.x < -128:
				player.x = GAME_WIDTH
			elif player.x > (GAME_WIDTH):
				player.x = -128
			
			#screen.fill(BLACK)
			#pygame.draw.rect(screen,GREEN, [lead_x,lead_y,10,10])
					#screen.fill(RED, rect=[200,200,50,50])
			
			screen.blit(bg, [0,0])	
			screen.blit(cat.img, [cat.x,cat.y]) #TODO: 
			#pygame.draw.rect(screen,BLUE, [catch_x,catch_y,100,10])
			screen.blit(player.img, [player.x,player.y])
			
			#pygame.draw.rect(screen,GREEN, [player.hitbox_x,player.hitbox_y, player.hitbox_width,player.hitbox_height])
						
			
			for t in things:
				#pygame.draw.rect(screen,GREEN, [t.x,t.y,10,10])
				screen.blit(t.img, [t.x,t.y])	
				#pygame.draw.rect(screen,GREEN, [t.hitbox_x,t.hitbox_y, t.hitbox_width,t.hitbox_height])
				
				if(cat.type == 'green' and cat.specialTime > 0): #TODO
					cat.specialTime -= 1
					t.speed = 6
					
				if(cat.type == 'pink' and cat.specialTime > 0): #TODO
					cat.specialTime -= 1
					print(t.speedX)
					t.x += t.speedX
					if(t.x < 0):
						t.x = 0
					elif(t.x >= GAME_WIDTH-48):
						t.x = GAME_WIDTH-48
						
				if slow_time > 0:
					t.y += (t.speed - 2)
					t.hitbox_y += (t.speed - 2)		
				else:
					t.y += t.speed
					t.hitbox_y += t.speed
				if t.y >= GAME_HEIGHT:
					things.remove(t)
					explosion.play()
					if lives == 0:
						gs = GameState.GAMEOVER
						pygame.mixer.music.stop()
					else:
						lives -= 1
				elif t.x >= player.x and t.x <= player.x + 100 and t.y >= player.y and t.y <= player.y + 10 :
					#print("Collison")
					catch.play()
					things.remove(t)
					score += 10 
					if star_time > 0:
						score += 10 
					#pygame.time.delay(2000)
					
			if powerups: 		
				for p in powerups:
					screen.blit(p.img, [p.x,p.y])	
					#pygame.draw.rect(screen,GREEN, [t.hitbox_x,t.hitbox_y, t.hitbox_width,t.hitbox_height])
					if slow_time > 0:
						p.y += (p.speed - 2)
						#p.hitbox_y += (p.speed - 2)
					else:
						p.y += p.speed
						#p.hitbox_y += p.speed
					if p.y >= GAME_HEIGHT:
						powerups.remove(p)
						explosion.play()
					elif p.x >= player.x and p.x <= player.x + 100 and p.y >= player.y and p.y <= player.y + 10 :
						#print("Collison")
						if p.type == "live":
							lives += 1
						if p.type == "star":
							star_time += 6
						if p.type == "slow":
							slow_time += 5
						powerups.remove(p)
						powerup.play()
						#pygame.time.delay(2000)
						
			if(cat.type == 'black' and cat.specialTime > 0):
				cat.specialTime -= 1
				screen.fill(BLACK)						
					
					
			screen_text = h3.render(str(sec), True, BLACK)
			t_size  = h3.size(str(sec))
			screen.blit(screen_text, [(156-t_size[0]),546]) #TODO:
			
			screen.blit(time, [5,546]) #TODO:
			screen.blit(frame, [65,546]) #TODO:
			
			
			screen_text = h3.render(str(score), True, BLACK)
			t_size  = h3.size(str(score))
			screen.blit(screen_text, [(456-t_size[0]),546]) #TODO:
			
			screen.blit(frame, [360,546]) #TODO:
			screen.blit(star, [300,546]) #TODO:
			
			
			screen_text = h3.render(str(lives), True, BLACK)
			t_size  = h3.size(str(lives))
			screen.blit(screen_text, [(720-t_size[0]),546]) #TODO:
			
			screen.blit(live, [570,546]) #TODO:
			screen.blit(frame, [630,546]) #TODO:
				
						
			#print(things)    
			pygame.display.flip()
			#print(clock.get_fps())
			
		
		gameover = pygame.image.load("assets/game_over.png")	
		gameover_sound = pygame.mixer.Sound("sounds/gameover.wav")
		gameover_sound.play()
		# Gameover Screen
		while gs == GameState.GAMEOVER:
			screen.fill(BLACK)
			screen.blit(gameover, [0,0])
			
			#gameover_text = "GAME OVER"
			#screen_text = h1.render(gameover_text, True, RED)
			#t_size  = h1.size(gameover_text)
			#screen.blit(screen_text, [(GAME_WIDTH/2)-t_size[0]/2,(GAME_HEIGHT/2)-t_size[1]/2])	
			
			score_text = "Time: " + str(sec) + " Score: " + str(score)
			screen_text = h4.render(score_text, True, WHITE)
			t_size  = h4.size(score_text)
			screen.blit(screen_text, [(GAME_WIDTH/2)-t_size[0]/2,(GAME_HEIGHT/2)-(t_size[1]/2)+100])
			
			playagain_text = "Press ENTER to play again"
			screen_text = h3.render(playagain_text, True, WHITE)
			t_size  = h3.size(playagain_text)
			
			count += 1
			if count % 2 == 0:
				screen.blit(screen_text, [(GAME_WIDTH/2)-t_size[0]/2,(GAME_HEIGHT/2)-(t_size[1]/2)+140])
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gs = GameState.EXIT		
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
						gs = GameState.RUN
						pygame.mixer.music.play(-1)
					
			pygame.display.flip()
			clock.tick(2)


if __name__ == '__main__':
	main()


