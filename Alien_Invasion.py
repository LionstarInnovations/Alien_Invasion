#############################################################
#     @author Marcus McFarlane          		  		        	#
#     Alien invasion with Pygame                  			    #
#                                                 			    #
#     Sounds from Soundbible.com                  			    #
#     Spaceship image from millionthvector.blogspot.com     #
#     credit image from upload.wikimedia.org                #
#############################################################



# Importing all necessary modules
import pygame, sys, random, time, os
from pygame.locals import *


# Initializing pygame 
pygame.init()

# Setting a variable to store pygame's clock for event timing 
clock = pygame.time.Clock()

# Loads the specified sound
intro_sound = pygame.mixer.Sound('intro_sound.wav')
gunshot = pygame.mixer.Sound('gunshot.wav')
explosion = pygame.mixer.Sound('explosion.wav')
# Screen width and height
screen_width = 800
screen_height = 600



# Setting the screen mode, caption and converting image 
screen = pygame.display.set_mode( (screen_width, screen_height), 0, 32)
pygame.display.set_caption ('Alien invasion')

# Error handler
try:
    intro_image = pygame.image.load('start_img.jpg').convert()
    credit_image = pygame.image.load('outside_space.jpg').convert()
    level_image = pygame.image.load('level_img.jpg').convert()
    ship = pygame.image.load('ship_up.png').convert_alpha()
    jet = pygame.image.load('jet_up.png').convert_alpha()
    jet2 = pygame.image.load('jet2.png').convert_alpha()
    jet_right = pygame.image.load('jet_right.png').convert_alpha()
    error_img = pygame.image.load('space_shuttle.jpg').convert_alpha()
except pygame.error:
    intro_image = pygame.image.load('space_shuttle.jpg').convert()
    credit_image = pygame.image.load('instruction_img.jpg').convert()
    level_image = pygame.image.load('level_img.jpg').convert()
    

# Storing colour variables
aqua = (0, 255, 255)
blue = (0, 0, 255, 255)
green = (0,255,0)
magenta = (255,51,153)
orange = (255, 128, 0)
pink = (255, 153, 153)
violet = (102,0,204)
white = (255, 255, 255)
yellow = (255, 255, 0)


# Defines pause function as false
pause = False

# Defining a class to contain all functions
class my_functions(object):
    def error_page():
        intro_sound.play()
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
            screen.blit(error_img,(0,0))
            
            # Running functions for the button menu
            my_functions.button("Play game ", 24,300,128,50,violet,blue,my_functions.level1)
            my_functions.button("Instruction",24,360,128,50,violet,blue,my_functions.help_text)
            my_functions.button("Credits",24,420,128,50,violet,blue,my_functions.credit_menu)
            my_functions.button("Exit game",24,480,128,50,violet,blue,my_functions.exit_game)


            pygame.display.update()
            clock.tick(30)
    
    # Defining the introduction menu function
    def introduction_menu():
        #Plays the loaded sound imediately it is run
        intro_sound.play()
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
            screen.blit(intro_image,(0,0))
            
            # Running functions for the button menu
            try:
                my_functions.button("Play game", 24,300,128,50,violet,blue,my_functions.story_mode)
                my_functions.button("Instruction",24,360,128,50,violet,blue,my_functions.help_text)
                my_functions.button("Credits",24,420,128,50,violet,blue,my_functions.credit_menu)
                my_functions.button("Exit game",24,480,128,50,violet,blue,my_functions.exit_game)
            except AttributeError:
               my_functions.error_page()

            pygame.display.update()
            clock.tick(30)

    # The pygame introduction menu
    def pygame_intro():
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
            #Runs the introduction_menu function
            my_functions.introduction_menu()


                
    # Defining the text properties for objects #
    #Takes arguments text, font and colour
    def text_properties(text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()


    def stats(font, size, color,  x, y, text):
        myfont = pygame.font.SysFont(font, size)
        label = myfont.render(text, 1, color)
        screen.blit(label, (x, y))
        
        
                                 
    # Defining a message function to display any text in specified style
    # Takes arguments (font name, pixel size, colour, x,y co-ordinate, text to display)
    def display_message(font, size, color,  x, y, text):
        myfont = pygame.font.SysFont(font, size)
        label = myfont.render(text, 1, color)
        x = ( (screen_width/2) - label.get_width()/2 )
        screen.blit(label, (x, y))


    # Button function for various actions
    def button(text,x,y,width,height,ic,ac, action=None):
        ''' x and y coordinates, ic = inactive color, ac = active color, action'''
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
       
        

        if x+width > mouse[0] > x and y+height > mouse[1] > y:
            pygame.draw.rect(screen, ac,(x-4,y-4,width+8,height+8))

            if click[0] == 1 and action != None:
                
                action()
                
                
        else:
            pygame.draw.rect(screen, ic,(x,y,width,height))

        smallText = pygame.font.SysFont("Calibri",20)
        textSurf, textRect = my_functions.text_properties(text, smallText, white)
        textRect.center = ( (x+(width/2)), (y+(height/2)) )
        screen.blit(textSurf, textRect)  

    def story_mode():
        running = True
        while running:
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                          
            screen.blit(level_image,(0,0))
            
            my_functions.display_message('calibri', 22, yellow,  143, 90, 'In the year 10,000 NRE (Never really existed) when there')
            my_functions.display_message('calibri', 22, yellow,  142, 120, 'arose out of a distant galaxy, Xhaka the lord of Alienopolis,')
            my_functions.display_message('calibri', 22, yellow,  143, 180, 'war was declared on Earth. To be conquered, to be ruled')
            my_functions.display_message('calibri', 22, yellow,  142, 210, 'to make humanity slaves to residents of the other galaxy')
            my_functions.display_message('calibri', 22, yellow,  172, 240, 'but Humanity would never succumb to such treats.')
            my_functions.display_message('calibri', 22, yellow,  132, 300, 'Special fleets have been sent to space to fight the remaining')
            my_functions.display_message('calibri', 22, yellow,  93, 330, 'enemy spaceships but they\'ve all been captured except your division. ')
            my_functions.display_message('calibri', 22, yellow,  162, 390, 'With all hope lost and humanity on the verge of doom')
            my_functions.display_message('calibri', 22, yellow,  113, 420, 'The fate of mankind lies in your hand. Save them or doom them?')

            my_functions.button("Play Now", 650,530, 128,50,violet,blue,my_functions.level1)
            screen.blit(ship, (80, 30))
            screen.blit(jet_right, (320, 480))
            screen.blit(jet, (700, 220))
            
            pygame.display.update()
        
            
            #clock.tick(30)
        
    def level1():
        
        def unpause():
            global pause
            pause = False
            

        def paused():
            while pause:
               
                my_functions.display_message('Arial', 50, green,  0, 200, 'Game Paused')
                my_functions.display_message('calibri', 30, green,  20, 270, 'Press C to continue or click the continue button')
                my_functions.button('Continue', 20,340, 128,50,violet,blue,unpause)
                my_functions.button('Exit game', 20,410, 128,50,violet,blue,my_functions.exit_game)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    
                    if event.type == pygame.KEYDOWN:
                
                        # unpause (not working)
                        if event.key == pygame.K_c:
                            unpause()
                            
                pygame.display.update()
                clock.tick(15)
       
        
        # Setting the screen mode, caption and converting image 
        screen = pygame.display.set_mode( (screen_width, screen_height), 0, 32)
        pygame.display.set_caption ('Level 1')

        level_image = pygame.image.load('level_img.jpg').convert()
        ship = pygame.image.load('ship_up.png').convert_alpha()
        jet = pygame.image.load('jet_up.png').convert_alpha()
        green_bullet = pygame.image.load('green_bullet.png').convert_alpha()

        # To generate random amount of enemies
        rand_amount = random.randint(10,20)

        class Alien(pygame.sprite.Sprite):
            """ This class represents the characters. """
            
            def __init__(self):
                # Call the parent class (Sprite) constructor
                super().__init__()
                
                # Loads and sets the Alien images
                self.image = ship
                
                # Fetch the rectangle object that has the dimensions of the image.
                self.rect = self.image.get_rect()
                
                    

            def reset_pos(self):
                """ Reset position to the top of the screen, at a random x and y location.
                Called by update() or the main program loop if there is a collision."""
                
                self.rect.x = random.randrange(5, 731)
                self.rect.y = random.randrange(-300, -70)
                player.health -=1



            def sprite_amount(amount):
                amount = rand_amount
                for i in range(amount):
                    # This represents a enemy
                    enemy = Alien()
                        
                    # Set a random location for the enemy
                    enemy.rect.x = random.randrange(5,700)
                    enemy.rect.y = random.randrange(-300, -20)
                    # Add the enemy to the list of objects
                    enemy_list.add(enemy)
                    all_sprites_list.add(enemy)
                

            def update(self):
                """ Called each frame. """
                # Move enemy down one pixel
                self.rect.y += 1
                # If enemy is too far down, reset to top of screen.
                if self.rect.y > 600:
                    self.reset_pos()
                    

         # Player's class       
        class Player(pygame.sprite.Sprite):
            """ This class represents the Player. """
            score = 0
            def __init__(self):
                """ Set up the player on creation. """
                # Call the parent class (Sprite) constructor
                super().__init__()
                health = self.health

                self.image = jet
                self.rect = self.image.get_rect()
                self.health = 100


            def move(self):
                # For moving the player
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.rect.centerx -= 20
                    if player.rect.bottomleft[0] <= 0:
                        player.health -= 1
                        player.rect.x += (player.rect.w)//2
                        
                           
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        player.rect.centerx += 20
                        if player.rect.bottomright[0] >= 800: 
                            player.health -= 2
                            player.rect.x -= (player.rect.w)//2
                            
                            
            def health(self):
                # Player's health
                self.health = health
                if self.health >= 100:
                    self.health = 100

                elif self.health < 100:
                    self.health += 5


            def GUI():
                if player.health >=70:
                    my_functions.stats('calibri', 25, green,  680,5, ('Health:' + str(player.health)))
                elif 40<= player.health <=69:
                    my_functions.stats('calibri', 25, yellow,  680,5, ('Health:' + str(player.health)))
                elif 1<= player.health <=39:
                    my_functions.stats('calibri', 25, magenta,  680,5, ('Health:' + str(player.health)))

                my_functions.stats('calibri', 25, green,  10,5, ('Score:' + str(player.score)))

                    
        # Bullet's class        
        class Bullet(pygame.sprite.Sprite):
            """ This class represents the bullet . """
            
            
            def __init__(self):
                # Call the parent class (Sprite) constructor
                super().__init__()
                self.image = green_bullet
                self.rect = self.image.get_rect()
                    
            def update(self):
                """ Move the bullet. """
                self.rect.y -= 5

            def game():
                enemy = Alien()
                for bullet in bullet_list:
                    for bullet in bullet_list:
                        
                        # See if it hit a enemy
                        enemy_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)
                        if enemy_hit_list:
                            explosion.play()
                            
                        # For each enemy hit, remove the bullet and add to the score
                        for enemy in enemy_hit_list:
                            bullet_list.remove(bullet)
                            all_sprites_list.remove(bullet)
                            player.score += 1

                        # Remove the bullet if it flies up off the screen
                        if bullet.rect.y < -10:
                            bullet_list.remove(bullet)
                            all_sprites_list.remove(bullet)


        # --- Sprite lists
        # This is a list of every sprite. All enemys and the player enemy as well.
        all_sprites_list = pygame.sprite.Group()
        # List of each enemy in the game
        enemy_list = pygame.sprite.Group()
        # List of each bullet
        bullet_list = pygame.sprite.Group()
        

        # --- Calls the sprite and takes an amount
        Alien.sprite_amount(10)
            
        # Creates an instance of the player and add it to the allsprites group
        player = Player()
        all_sprites_list.add(player)

        hero = pygame.sprite.Group()
        hero.add(player)
        
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        #Sets starting score
        score = player.score

        #Player's position
        player.rect.centery = 565
        player.rect.centerx = 400

        running = True
        global pause
        # Main Program Loop
        while running:
            # Event Processing
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                # Runs bullet function when key is pressed    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Play gunshot sound
                    gunshot.play()
                    # Creates an instance of bullet
                    bullet = Bullet()
                    # Set the bullet so it is where the player is
                    bullet.rect.centerx = player.rect.centerx
                    bullet.rect.centery = player.rect.centery
                    # Add the bullet to the lists
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # Play gunshot sound
                    gunshot.play()
                    
                    # Fire a bullet if the user clicks the mouse button
                    bullet = Bullet()
                    # Set the bullet so it is where the player is
                    bullet.rect.centerx = player.rect.centerx
                    bullet.rect.centery = player.rect.y
                    
                    # Add the bullet to the lists
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)

                # Manages keypad presses
                elif event.type == pygame.KEYDOWN:
                    player.move()

                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

                    # pause key
                    if event.key == pygame.K_p:
                        pause = True
                        
                        paused()
                        


                    # unpause
                    if event.key == pygame.K_c:
                        pause = False
                        unpause()                                
            
            # Call the update() method on all the sprites
            all_sprites_list.update()
            
            # Calculate mechanics for each bullet
            Bullet.game()

            # Checks for collision between player and aliens
            if pygame.sprite.groupcollide(hero, enemy_list, False, True):
                explosion.play()
                player.health-=20
                player.score  +=1

            # Check and change colour of player health depending on level
            screen.blit(level_image, (0,0))

            # Collision detection
            Player.GUI()
            

            # Draw all the spites
            all_sprites_list.draw(screen)
            
            # Update the screen with drawn images
            pygame.display.flip()
            
            # Limit to 30 frames per second
            clock.tick(30)

            if len(enemy_list) <= 0:
                my_functions.level2()

            if player.health <=0:
                my_functions.gameover()
        running = False
                

    def level2():
        def unpause():
            global pause
            pause = False
            

        def paused():
            while pause:
               
                my_functions.display_message('Arial', 50, green,  0, 200, 'Game Paused')
                my_functions.display_message('calibri', 30, green,  20, 270, 'Press C to continue or click the continue button')
                my_functions.button('Continue', 20,340, 128,50,violet,blue,unpause)
                my_functions.button('Exit game', 20,410, 128,50,violet,blue,my_functions.exit_game)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    
                    if event.type == pygame.KEYDOWN:
                
                        # unpause (not working)
                        if event.key == pygame.K_c:
                            unpause()
                            
                            
                            


                
                pygame.display.update()
                clock.tick(15)
       
        
        # Setting the screen mode, caption and converting image 
        screen = pygame.display.set_mode( (screen_width, screen_height), 0, 32)
        pygame.display.set_caption ('Level 2')

        level_image = pygame.image.load('level_img.jpg').convert()
        ship = pygame.image.load('ship2.png').convert_alpha()
        jet = pygame.image.load('jet2.png').convert_alpha()
        green_bullet = pygame.image.load('green_bullet.png').convert_alpha()

        # To generate random amount of enemies
        rand_amount = random.randint(20, 40)

        class Alien(pygame.sprite.Sprite):
            """ This class represents the characters. """
            
            def __init__(self):
                # Call the parent class (Sprite) constructor
                super().__init__()
                
                # Loads and sets the Alien images
                self.image = ship
                
                # Fetch the rectangle object that has the dimensions of the image.
                self.rect = self.image.get_rect()
                    

            def reset_pos(self):
                """ Reset position to the top of the screen, at a random x and y location.
                Called by update() or the main program loop if there is a collision."""
                
                self.rect.x = random.randrange(5, 731)
                self.rect.y = random.randrange(-300, -70)
                player.health -=10



            def sprite_amount(amount):
                #amount = rand_amount
                for i in range(amount):
                    # This represents a enemy
                    enemy = Alien()
                        
                    # Set a random location for the enemy
                    enemy.rect.x = random.randrange(5,700)
                    enemy.rect.y = random.randrange(-500, -70)
                    # Add the enemy to the list of objects
                    enemy_list.add(enemy)
                    all_sprites_list.add(enemy)
                

            def update(self):
                """ Called each frame. """
                # Move enemy down one pixel
                self.rect.y += 2
                # If enemy is too far down, reset to top of screen.
                if self.rect.y > 600:
                    self.reset_pos()
                    player.health -=10
                    

         # Player's class       
        class Player(pygame.sprite.Sprite):
            """ This class represents the Player. """
            
            score = 0
            def __init__(self):
                """ Set up the player on creation. """
                # Call the parent class (Sprite) constructor
                super().__init__()
                health = self.health

                self.image = jet
                self.rect = self.image.get_rect()
                self.health = 100


            def move(self):
                # For moving the player
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.rect.centerx -= 20
                    if player.rect.bottomleft[0] <= 0:
                        player.health -= 5
                        player.rect.x += (player.rect.w)//2
                        
                           
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        player.rect.centerx += 20
                        if player.rect.bottomright[0] >= 800: 
                            player.health -= 5
                            player.rect.x -= (player.rect.w)//2
                            
            def health(self):
                # Player's health
                #self.health = health
                if self.health >= 100:
                    self.health = 100

                elif self.health < 100:
                    self.health += 5


            def GUI():
                if player.health >=70:
                    my_functions.stats('calibri', 25, green,  680,5, ('Health:' + str(player.health)))
                elif 40<= player.health <=69:
                    my_functions.stats('calibri', 25, yellow,  680,5, ('Health:' + str(player.health)))
                elif 1<= player.health <=39:
                    my_functions.stats('calibri', 25, magenta,  680,5, ('Health:' + str(player.health)))

                my_functions.stats('calibri', 25, green,  10,5, ('Score:' + str(player.score)))

                    
        # Bullet's class        
        class Bullet(pygame.sprite.Sprite):
            """ This class represents the bullet . """
            
            
            
            
            def __init__(self):
                # Call the parent class (Sprite) constructor
                super().__init__()
                self.image = green_bullet
                self.rect = self.image.get_rect()
                    
            def update(self):
                """ Move the bullet. """
                self.rect.y -= 5

            def game(): 
                for bullet in bullet_list:
                    for bullet in bullet_list:
                        
                        # See if it hit a enemy
                        enemy_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)
                        if enemy_hit_list:
                            explosion.play()
                            
                        # For each enemy hit, remove the bullet and add to the score
                        for enemy in enemy_hit_list:
                            bullet_list.remove(bullet)
                            all_sprites_list.remove(bullet)
                            player.score += 5

                        # Remove the bullet if it flies up off the screen
                        if bullet.rect.y < -10:
                            bullet_list.remove(bullet)
                            all_sprites_list.remove(bullet)


        # --- Sprite lists
        # This is a list of every sprite. All enemys and the player enemy as well.
        all_sprites_list = pygame.sprite.Group()
        # List of each enemy in the game
        enemy_list = pygame.sprite.Group()
        # List of each bullet
        bullet_list = pygame.sprite.Group()
        

        # --- Calls the sprite and takes an amount
        
        Alien.sprite_amount(rand_amount)
            
        # Creates an instance of the player and add it to the allsprites group
        player = Player()
        all_sprites_list.add(player)

        hero = pygame.sprite.Group()
        hero.add(player)
        
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        #Sets starting score
        score = player.score

        #Player's position
        player.rect.centery = 565
        player.rect.centerx = 400

        running = True
        global pause
        # Main Program Loop
        while running:
            # Event Processing
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                # Runs bullet function when key is pressed    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Play gunshot sound
                    gunshot.play()
                    # Creates an instance of bullet
                    bullet = Bullet()
                    # Set the bullet so it is where the player is
                    bullet.rect.centerx = player.rect.centerx
                    bullet.rect.centery = player.rect.centery
                    # Add the bullet to the lists
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # Play gunshot sound
                    gunshot.play()
                    
                    # Fire a bullet if the user clicks the mouse button
                    bullet = Bullet()
                    # Set the bullet so it is where the player is
                    bullet.rect.centerx = player.rect.centerx
                    bullet.rect.centery = player.rect.y
                    
                    # Add the bullet to the lists
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)

                # Manages keypad presses
                elif event.type == pygame.KEYDOWN:
                    player.move()

                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

                    # pause key
                    if event.key == pygame.K_p:
                        pause = True
                        
                        paused()
                        


                    # unpause
                    if event.key == pygame.K_c:
                        pause = False
                        unpause()                                
            
            # Call the update() method on all the sprites
            all_sprites_list.update()
            
            # Calculate mechanics for each bullet
            Bullet.game()

            # Checks for collision between player and aliens
            if pygame.sprite.groupcollide(hero, enemy_list, False, True):
                explosion.play()
                player.health-=20
                player.score  +=5

            # Check and change colour of player health depending on level
            screen.blit(level_image, (0,0))

            # Collision detection
            Player.GUI()
            

            # Draw all the spites
            all_sprites_list.draw(screen)
            
            # Update the screen with drawn images
            pygame.display.flip()
            
            # Limit to 30 frames per second
            clock.tick(30)

            if len(enemy_list) <= 0:
                my_functions.winner()
            
                #my_functions.level2()
                #running = False

            if player.health <=0:
                my_functions.gameover()
        running = False
                        
    
    # Function to display the instruction menu
    def help_text():
        running = True
        while running:
            

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
            screen.blit(credit_image,(0,0))
            
            # Displays game objectives in the center
            my_functions.display_message('calibribold', 60, green,  231, 60, 'Your Objectives')
            my_functions.display_message('calibri', 22, yellow,  162, 150, 'The aim of the game is to defeat the Alien lord Xhaka')
            my_functions.display_message('calibri', 22, yellow,  172, 180, ' and his force with the available weapons present')

            # Display's game controls in the center                          
            my_functions.display_message('calibribold', 54, green,  310, 240, 'Controls')
            my_functions.display_message('Arial', 20, magenta,  310, 290, 'To move Left: \u2190 or A')
            my_functions.display_message('Arial', 20, magenta,  310, 320,  'To move Right: \u2192 or D')
            my_functions.display_message('Arial', 20, magenta,  310, 350, 'To shoot bullets: Left mouse click or Spacebar')
            my_functions.display_message('Arial', 20, magenta,  310, 380, 'To pause game: P')
            my_functions.display_message('Arial', 20, magenta,  310, 410, 'To Quit game: Q')


            
            # Display buttons on the screen
            my_functions.button("Home", 24,420,128,50,violet,blue,my_functions.pygame_intro)
            my_functions.button("Exit game",24,480,128,50,violet,blue,my_functions.exit_game) 

            # Fades sound after 5 seconds
            
            
            pygame.display.update()
            clock.tick(30)

#------------------------------------------------------------------------------------------
            
    def gameover():

        my_functions.display_message('calibribold', 50, magenta, 0,250, 'Gameover :(')
        my_functions.display_message('calibribold', 50, magenta, 0,320, 'You died and earth has been conquered')

        

        while True:
            for event in pygame.event.get():

                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


            my_functions.button("Restart Game", 24,420,128,50,violet,blue,my_functions.level1)
            my_functions.button("Exit game",24,480,128,50,violet,blue,my_functions.exit_game) 


            pygame.display.update()
            clock.tick(15)


    def winner():
            my_functions.display_message('calibribold', 50, magenta, 0,250, 'Congratulations :)')
            my_functions.display_message('calibribold', 50, magenta, 0,320, 'You have saved Planet earth')

            

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()


                my_functions.button("Replay", 24,420,128,50,violet,blue,my_functions.level1)
                my_functions.button("Exit game",24,480,128,50,violet,blue,my_functions.exit_game) 

                pygame.display.update()
                clock.tick(15)

    


   #--------------------------------------------------------------------------------------------------
    
    # Function to exit game   
    def exit_game():
        pygame.quit()
        sys.exit()
        quit()


  # ------------------------------------------------------------------------------------------------
  
    # Function to display the credit menu
    def credit_menu():
        # Loops to keep game running and exit when (X) button is clicked
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
            
            # Blits the image to the screen
            screen.blit(credit_image,(0,0))

            #Centered it using a cm coordinate and converting to pixel
            #formula 400 - 19.8x, x values in centimeters
            #Button takes (font type, pixel size, color, x,y co-ordinate, text to display)
            my_functions.display_message('calibribold', 60, green,  320, 80, 'Credits')
            my_functions.display_message('Arialbold', 32, aqua,  266, 150, 'Created by: Taiwo Kareem')
            my_functions.display_message('Arialbold', 32, aqua,  340, 180, 'Marcus McFarlane')
            my_functions.display_message('calibri', 18, yellow,  324, 230, 'Alien Invasion')
            my_functions.display_message('calibri', 12, yellow,  428, 250, 'v 1.0.0')
            my_functions.display_message('calibribold', 35, pink,  324, 280, 'Used files (References)')
            my_functions.display_message('calibri', 14, magenta,  428, 320, 'sounds from www.soundbible.com')
            my_functions.display_message('calibri', 14, magenta,  428, 340, 'images from www.millionthvector.blogspot.com')
            my_functions.display_message('calibri', 14, magenta,  428, 360, 'images from upload.wikimedia.org')
            
            my_functions.button("Home", 24,420,128,50,violet,blue,my_functions.pygame_intro)
            my_functions.button("Exit game",24,480,128,50,violet,blue,my_functions.exit_game) 

            # Fades sound after 5 seconds
            pygame.mixer.music.fadeout(5000)

            #Updates the display and next line runs in 30 frames per second
            pygame.display.update()
            clock.tick(30)     


#----------------------------------------------------------------------
# Main start menu loop
running = True
while running:
    my_functions.pygame_intro()
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.update()
