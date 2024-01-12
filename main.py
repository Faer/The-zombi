import pygame
import time
import random

pygame.init()
screen = pygame.display.set_mode()

player = pygame.Surface((50, 50))
player.fill("blue")

button_left = pygame.Surface((150 ,300))
button_left.fill((255, 255, 255))

button_right = pygame.Surface((150 ,300))
button_right.fill((255, 255, 255))

button_up = pygame.Surface((150 ,300))
button_up.fill((255, 255, 255))

button_down = pygame.Surface((150 ,300))
button_down.fill((255, 255, 255))

point_tabls = pygame.Surface((100,290))
point_tabls.fill((255, 255, 255))

zombi = pygame.Surface((50 ,50))
zombi.fill((255,0,0))

apple = pygame.Surface((40, 40))
apple.fill((0,255,0))

txt = pygame.font.Font(None, 70)
txt_big = pygame.font.Font(None, 90)
txt_big_big = pygame.font.Font(None, 200)
left_txt = txt.render("LEFT", False,  (0, 0, 0))
right_txt = txt.render("RIGHT", False,  (0, 0, 0))
up_txt = txt.render("UP", False,  (0, 0, 0))
down_txt = txt.render("DOWN", False,  (0, 0, 0))
game_over_txt = txt_big_big.render("Вы умерли.", False,  (255,255,255))
game_over_restart_txt = txt_big_big.render("Начать заново?", False,  (255,255,255))
game_over_restart__txt = txt_big_big.render("Нажми:^^^^^^^", False,  (50,50,50))
exit_txt = txt_big_big.render("Загрузка...", False,  (255,255,255))

x_player = 500
y_player = 500
x_zombi = 1500
y_zombi = 500
x_left = True
x_right = True
y_up = True
y_down = True
running = True
gameplay = True
point_win = False
apple_ = True
x_zombi_ = 0
y_zombi_ = 0
point = 0 - 2
point_minus = 0
point_game_over = 0
exit = False
exit_1 = True
apple__ = False
x_apple = 0
y_apple = 0
time_ = 0

left_txt  = pygame.transform.rotate(left_txt, -90)
right_txt  = pygame.transform.rotate(right_txt, -90)
up_txt  = pygame.transform.rotate(up_txt, -90)
down_txt  = pygame.transform.rotate(down_txt, -90)
game_over_txt  = pygame.transform.rotate(game_over_txt, -90)
game_over_restart_txt  = pygame.transform.rotate(game_over_restart_txt, -90)
game_over_restart_txt  = pygame.transform.rotate(game_over_restart_txt, -90)
exit_txt  = pygame.transform.rotate(exit_txt, -90)

point_timer = pygame.USEREVENT + 1
pygame.time.set_timer(point_timer, 1000)

while running:
	mouse = pygame.mouse.get_pos()
	
	screen.fill("black")
	screen.blit(player, (y_player, x_player))
	screen.blit(zombi, (y_zombi + y_zombi_, x_zombi + x_zombi_))
	screen.blit(button_left,(50, 50))
	screen.blit(left_txt,(95, 150))
	screen.blit(button_right,(50, 400))
	screen.blit(right_txt, (95, 475))
	screen.blit(button_up,(50, 1350))
	screen.blit(up_txt, (95, 1470))
	screen.blit(button_down, (50, 1700))
	screen.blit(down_txt, (95, 1777))
	screen.blit(point_tabls, (50, 855))
	
	player_rect = player.get_rect(topleft=(y_player, x_player))
	
	if apple_:
		x_apple = random.randint(20, 1970)
		y_apple = random.randint(210, 1020)
		apple__ = True
		apple_ = False
		
	if apple__ == True:
		apple_rect = apple.get_rect(topleft=(y_apple, x_apple))
			
		screen.blit(apple, (y_apple, x_apple))
		
		if player_rect.colliderect(apple_rect):
			apple_ = True
			point -= 2
	
	if exit == True:
		time.sleep(2)
		exit = False
	if exit_1 == True:
		exit = True
		screen.fill(("black"))
		screen.blit(exit_txt, (500,650))
		exit_1 = False
	
	game_over_restart_rect = game_over_restart_txt.get_rect(topleft=(500, 625))
	
	button_left_rect = button_left.get_rect(topleft=(50,50))
	button_right_rect = button_right.get_rect(topleft=(50,400))
	button_up_rect = button_up.get_rect(topleft=(50, 1350))
	button_down_rect = button_down.get_rect(topleft=(50, 1700))
	
	if gameplay:

		point_txt = txt_big.render(str(point),False, (0,0,0))
		timer_txt = txt_big.render(str(time_),False, (0,0,0))
		
		point_txt  = pygame.transform.rotate(point_txt, -90)
		
		screen.blit(point_txt, (70, 860))
	
		zombi_rect = zombi.get_rect(topleft=(y_zombi + y_zombi_, x_zombi + x_zombi_))
		
		point_minus = (point / 12) + 1
		
		if y_zombi > y_player:
			y_zombi -= point_minus
		if y_zombi < y_player:
			y_zombi += point_minus
			
		if x_zombi > x_player:
			x_zombi -= point_minus
		if x_zombi < x_player:
			x_zombi += point_minus
		
		if player_rect.colliderect(zombi_rect):
			gameplay = False
	
		if button_left_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
			button_left.fill((155, 155, 155))
			if x_left == True:
				x_player -= 4.5
		else:
			button_left.fill((255, 255, 255))
	
		if button_right_rect.collidepoint(mouse) and 	pygame.mouse.get_pressed()[0]:
			button_right.fill((155, 155, 155))
			if x_right == True:
				x_player += 4.5
		else:
			button_right.fill((255, 255, 255))
		
		if button_up_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
			button_up.fill((155, 155, 155))
			if y_up == True:
				y_player += 4.5
		else:
			button_up.fill((255, 255, 255))
		
		if button_down_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
			button_down.fill((155, 155, 155))
			if y_down == True:
				y_player -= 4.5
		else:
			button_down.fill((255, 255, 255))
			
		if x_player > 1975:
			x_right = False
		else:
			x_right = True
			
		if x_player < 10:
			x_left = False
		else:
			x_left = True
			
		if y_player > 1020:
			y_up = False
		else:
			y_up = True
			
		if y_player < 210:
			y_down = False
		else:
			y_down = True
			
	else:
		if time_ > point_game_over:
			point_game_over = time_
		game_over_point_txt = txt_big_big.render("Время макс: " + str(point_game_over), False,  (255,255,255))
		game_over_point_txt  = pygame.transform.rotate(game_over_point_txt, -90)
		x_player = 500
		y_player = 500
		x_zombi = 1500
		y_zombi = 500
		time_ = 0
		apple_ = True
		x_left = True
		x_right = True
		y_up = True
		y_down = True
		x_zombi_ = 0
		y_zombi_ = 0
		point = 0
		point_minus = 0
		screen.fill("black")
		screen.blit(game_over_txt, (700, 630))
		screen.blit(game_over_restart_txt, (500, 480))
		screen.blit(game_over_restart__txt, (300, 480))
		screen.blit(game_over_point_txt, (20,515))
		if game_over_restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
			gameplay = True
		
	pygame.display.update()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
		if event.type == point_timer:
			point += 1
			time_ += 1