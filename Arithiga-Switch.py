
from ship import Ship
from numbers import Numbers
from operators import Operators

import pygame
from pygame.locals import *
from sys import exit
import os.path as osp

from random import *

class GalagaVariant: # tentative title

    def __init__(self):

        pygame.init()

        pygame.mixer.init()

        pygame.display.set_caption("Arithiga")

        self.screen = pygame.display.set_mode((640,480),0,32)

        self.screen.fill([0, 0, 0]) # background will be black

    # Parameter testing, not used for now
    def Parameters(self):

        # self.background_color
        # self.number_font
        # self.chosen_number_colors (array)
        # self.avatar
        # self.final_laser_choice

        selection_font = pygame.font.SysFont('arial', 20)

        intro_directions = selection_font.render("Press the n key to cycle through the options", True, (250, 50, 0), (0, 0, 0))
        intro_directions2 = selection_font.render("Press the space key to select your choice or continue", True, (250, 50, 0), (0,0,0))
        intro_directions3 = selection_font.render("To the next screen", True, (250, 50, 0), (0,0,0))

        pygame.display.flip()

        while True:

            self.screen.blit(intro_directions, (125, 100))
            self.screen.blit(intro_directions2, (75, 150))
            self.screen.blit(intro_directions3, (220, 200))
            pygame.display.flip()

            event = pygame.event.wait()

            if event.type is pygame.QUIT:
                sys.exit()

            if event.type is pygame.KEYDOWN:

                if event.key is K_SPACE:
                    break

            self.screen.fill([0,0,0])

        self.screen.fill([0,0,0])

        background_colors = [(0,0,0), (255, 212, 0), (255, 157, 255), (106, 185, 132), (255, 255, 255), (255, 255, 0)]

        which_back_color = selection_font.render("Which background color would you like to use?", True, (250, 50, 0), (0, 0, 0))

        pygame.display.flip()
        locations = [100, 200, 300, 400, 500, 600]
        option = 0
        back_color_count = 0
        circle_count = 0

        while True:

            self.screen.blit(which_back_color, (100, 100))

            count = 0

            for color in background_colors:
                count += 1
                pygame.draw.rect(self.screen, color, pygame.Rect(100 * count, 300, 30, 30))

            pygame.draw.circle(self.screen, (255, 255, 255), (locations[option], 300), 3)

            circle_count += 1
            pygame.display.update()

            if circle_count == 30:
                self.screen.fill([0,0,0])
                back_color_count += 1
                circle_count = 0

                if back_color_count == 6:
                    option = 0
                    back_color_count = 0

                else:
                    option += 1 

            event = pygame.event.wait()

            if event.type is pygame.QUIT:
                sys.exit()

            if event.type is pygame.KEYDOWN:

                if event.key is K_SPACE:
                    self.background_color = background_colors[option]
                    break              

        self.screen.fill([0,0,0])

        font_choices = ['impact', 'arial', 'silom', 'corbel', 'optima']

        option = 0
        font_count = 0

        while True:

            event = pygame.event.wait()

            if event.type is pygame.QUIT:
                sys.exit()

            if event.type is pygame.KEYDOWN:

                if event.key is K_n:
                    self.screen.fill([0,0,0])

                    font_count += 1

                    if font_count == 5:
                        option = 0
                        font_count = 0

                    else:
                        option += 1

                if event.key is K_SPACE:
                    self.number_font = font_choices[option]
                    break

            which_font = selection_font.render("Which font do you want to use for the numbers?", True, (200, 50, 0), (0, 0, 0))

            current_font = pygame.font.SysFont(font_choices[option], 20)

            number = current_font.render('5', True, (200, 50, 0), (0, 0, 0))

            self.screen.blit(which_font, (50, 100))

            self.screen.blit(number, (300, 300))
            
            pygame.display.update()

        number_colors = [(255, 255, 255), (255, 212, 0), (255, 157, 255), (106, 185, 132), (0,0,0), (255, 255, 0), (201, 103, 255), (233, 54, 0), (0, 247, 194), (216, 164, 95), (73, 133, 246)]

        self.chosen_number_colors = []

        self.final_number_font = pygame.font.SysFont(self.number_font, 20)

        number_color_counter = 0

        for number in range(0,10):

            self.screen.fill([0,0,0])
            option = 0

            while True:

                event = pygame.event.wait()

                if event.type is pygame.QUIT:
                    sys.exit()

                if event.type is pygame.KEYDOWN:

                    if event.key is K_n:
                        self.screen.fill([0,0,0])

                        number_color_counter += 1
                        
                        if number_color_counter == 11:
                            option = 0
                            number_color_counter = 0

                        else:
                            option += 1

                    if event.key is K_SPACE:
                        self.chosen_number_colors.append(number_colors[option])
                        break

                which_number_color = selection_font.render("For each number, what color do you want?", True, (200, 50, 0), (0, 0, 0))

                self.screen.blit(which_number_color, (50, 100))

                the_number = self.final_number_font.render(str(number), True, number_colors[option], self.background_color)
                self.screen.blit(the_number, (300, 300))
                pygame.display.update()

        self.screen.fill([0,0,0])
        # Select the type of ship you want

        ship_option = pygame.image.load("galaga-ship.jpg").convert_alpha()
        bug_option = pygame.image.load("bug.jpg").convert_alpha()
        ghost_option = pygame.image.load("ghost.jpg").convert_alpha()

        avatar_options = [ship_option, bug_option, ghost_option]

        locations = [150, 300, 450]
        option = 0
        avatar_count = 0

        while True:

            which_avatar = selection_font.render("Which avatar would you like to use?", True, (200, 50, 0), (0, 0, 0))

            self.screen.blit(which_avatar, (100, 100))

            count = 0
            for avatar in avatar_options:
                count += 1
                self.screen.blit(avatar_options[count - 1], (150 * count, 300))

            pygame.draw.circle(self.screen, (255, 255, 255), (locations[option], 300), 3)

            pygame.display.flip()

            event = pygame.event.wait()

            if event.type is pygame.QUIT:
                sys.exit()

            if event.type is pygame.KEYDOWN:

                if event.key is K_n:
                    avatar_count += 1
                    if avatar_count == 3:
                        option = 0
                        avatar_count = 0

                    else:
                        option += 1

                if event.key is K_SPACE:
                    self.avatar = avatar_options[option]
                    break

            self.screen.fill([0,0,0])

        self.screen.fill([0,0,0])

        self.initialize()

    def initialize(self):

        # Sets up the numbers and operators that move down the screen.

        self.answer_numbers = [4, 13, 21, 34, 48, 64, 85, 110] # possible answers for game, ideally will randomize in final game

        # Creates objects for each number
        self.number_objects = []

        for number in range(1,10):

            image = self.final_number_font.render(str(number), True, self.chosen_number_colors[number])
            new_number = Numbers(self.screen, image, number, False)
            self.number_objects.append(new_number)

        plus_image = pygame.image.load("plussymbol.png").convert_alpha()
        minus_image = pygame.image.load("minussymbol.png").convert_alpha()
        multiply_image = pygame.image.load("multiplysymbol.png").convert_alpha()
        divide_image = pygame.image.load("dividesymbol.png").convert_alpha()
        power_image = pygame.image.load("caret.png").convert_alpha()

        # Creates objects for each operator (may remove minus and divide)
        self.plus = Operators(self.screen, plus_image, '+', False)
        self.minus = Operators(self.screen, minus_image, '-', False)
        self.multiply = Operators(self.screen, multiply_image, '*', False)
        self.divide = Operators(self.screen, divide_image, '/', False)
        self.power = Operators(self.screen, power_image, '^', False)

        # A lot of initializations
        self.hit_number = False

        self.hit_operator = False

        self.points = 0

        self.temporary_operator = '+' # Initalizes the operator

        self.temporary_number = 0

        self.answer_numbers_index = 0 # Defines current answer player strives for. Increments everytime the correct answer is chosen

        self.accumulating_answer = 0 # Keeps track of current value user calculates after shooting the numbers and operators.

        self.number_operators_used = 0 # Keeps track of number of operators used (for points)

        self.random_operator_count = 0  # Determines when operator will appear, spaces them out with 

        self.random_number_count = 0

        self.x = 319
        self.y = 350

        self.player_ship = Ship(self.screen, self.avatar, self.x, self.y)

        self.ships = pygame.sprite.Group()
        self.ships.add(self.player_ship)

        self.present_numbers_operators = pygame.sprite.Group()

        self.stop_moving = False

        self.x_positions = []

        self.introMenu()

    # Conducts operation of inputed values
    def Operation(self, temporary_operator, temporary_number_one, temporary_number_two):

        if temporary_operator == '+':
            return (temporary_number_one + temporary_number_two)
        elif temporary_operator == '-':
            return (temporary_number_one - temporary_number_two)
        elif temporary_operator == '*':
            return (temporary_number_one * temporary_number_two)
        elif temporary_operator == '/':
            return (temporary_number_one / temporary_number_two)
        else:
            return (temporary_number_one ** temporary_number_two)

    def introMenu(self):

        self.screen.fill(self.background_color)

        font = pygame.font.SysFont('impact', 40)

        text = font.render("Arithiga", True, (200, 50, 0))

        self.screen.blit(text, (250, 50))

        font2 = pygame.font.SysFont('arial', 25)
        text2 = font2.render("Press the Space to Start", True, (200, 50, 0))

        self.screen.blit(text2, (250, 240))

        pygame.display.flip()

        while True:
    
            event = pygame.event.wait()

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    self.Directions()

    def endGame(self):

        self.screen.fill(self.background_color)

        end_font = pygame.font.SysFont('arial', 25)
        end_text = end_font.render("Game Over", True, (200, 50, 0))

        continue_text = end_font.render("Press f to Continue", True, (200, 50, 0))
        quit_text = end_font.render("Press q to Quit", True, (200, 50, 0))

        self.screen.blit(end_text, (310, 180))

        pygame.display.flip()

        pygame.time.wait(1100)

        self.screen.blit(continue_text, (310, 211))

        self.screen.blit(quit_text, (310, 250))

        pygame.display.flip()

        while True:

            event = pygame.event.wait()

            if event.type is pygame.KEYDOWN:

                if event.key is pygame.K_f:
                    self.initialization()

                if event.key is pygame.K_q:
                    sys.exit()

            if event.type is pygame.QUIT:
                sys.exit()

    def Directions(self):

        self.screen.fill(self.background_color)

        directions_font = pygame.font.SysFont('arial', 15)
        
        direction_text = directions_font.render("Press the Space Key When the Ship is Beneath the Number/Operator You Want", True, (200,50,0))

        direction_text2 = directions_font.render("Choose The Numbers and Operators to Get the Given Number!", True, (200, 50, 0))

        self.screen.blit(direction_text, (80, 180))

        self.screen.blit(direction_text2, (100, 200))

        pygame.display.flip()

        while True:
    
            event = pygame.event.wait()

            if event.type is pygame.QUIT:
                sys.exit()

            if event.type is pygame.KEYDOWN:

                if event.key is pygame.K_SPACE:
                    self.run()

    # Updates info on top of the screen.
    def changeInfo(self):

        info_font = pygame.font.SysFont('arial', 18)
        answer_text = info_font.render("Current Number: " + str(self.answer_numbers[self.answer_numbers_index]), True, (200, 50, 0))

        self.screen.blit(answer_text, (325, 40))

        number_of_lives_text = info_font.render("Current Lives: " + str(self.player_ship.CurrentLives()), True, (200,50,0))
        self.screen.blit(number_of_lives_text, (180, 40))

        accumulating_text = info_font.render("Current Result: " + str(self.accumulating_answer), True, (200, 50, 0))

        self.screen.blit(accumulating_text, (25, 40))

        points_text = info_font.render("Current Points: " + str(self.points), True, (200,50,0))
        self.screen.blit(points_text, (490, 40))

    # Runs the game
    def run(self):

        pygame.time.set_timer(pygame.USEREVENT, 50)

        self.screen.fill(self.background_color)

        choice = 0
        count_choice = 0
        can_set = False
        first_time = True
        second_time = False

        while True:

            event = pygame.event.wait()

            if event.type is pygame.QUIT:
                print 'quit'
                sys.exit()

            if event.type is pygame.KEYDOWN:

                if event.key is K_SPACE:

                    if self.stop_moving:
                        self.stop_moving = False
                    elif not self.stop_moving:
                        self.stop_moving = True
            
            if event.type is not pygame.USEREVENT:
                continue

            random_value = int(random() * 9.9)  # Randomizes what number appears at the top
            
            random_operator = random() * 5  # Randomizes what operator appears at the top

            start_position_operator = 610.0 * random() # Randomizes where the number will appear at the top

            start_position_number = 610.0 * random() # Randomizes where the operator will appear at the top

            # For loop instead?

            self.random_number_count += 1
                
            # Series of if-else statements to initalize movment of a number given the random value

            count_choice += 1

            if (not self.hit_number) or second_time:

                if len(self.present_numbers_operators) < 3:

                    if self.present_numbers_operators != start_position_number:

                        if (not self.number_objects[random_value].moving()):
                            self.number_objects[random_value].setXPosition(start_position_number)
                            self.number_objects[random_value].toggle()

                        self.x_positions.append(start_position_number)

                        print "adding"

                    can_set = True

                else:

                    if second_time:
                        self.hit_number = True
                        self.hit_operator = True
                        second_time = False
                        can_set = False

                    elif (not second_time) and can_set:

                        self.hit_number = True
                        self.hit_operator = False

                        can_set = False

            elif not self.hit_operator:

                if len(self.present_numbers_operators) < 3:

                    if (not self.plus.moving()) and random_operator > 0 and random_operator <= 1:
                        self.plus.setXPosition(start_position_operator)
                        self.present_numbers_operators.add(self.plus)
                        self.plus.toggle()

                    elif (not self.minus.moving()) and random_operator > 1 and random_operator <= 2:
                        self.minus.setXPosition(start_position_operator)
                        self.present_numbers_operators.add(self.minus)
                        self.minus.toggle()

                    elif (not self.multiply.moving()) and random_operator > 2 and random_operator <= 3: 
                        self.multiply.setXPosition(start_position_operator)
                        self.present_numbers_operators.add(self.multiply)
                        self.multiply.toggle()

                    elif (not self.divide.moving()) and random_operator > 3 and random_operator <= 4:
                        self.divide.setXPosition(start_position_operator)
                        self.present_numbers_operators.add(self.divide)
                        self.divide.toggle()

                    elif (not self.power.moving()) and random_operator > 4 and random_operator <= 5:
                        self.power.setXPosition(start_position_operator)
                        self.present_numbers_operators.add(self.power)
                        self.power.toggle()

                    self.x_positions.append(start_position_operator)

                    print "adding"

                    can_set = True

                else:

                    if can_set:
                        
                        self.hit_number = False
                        self.hit_operator = True
                        can_set = False

            # Reduce the number of lives everytime the ship hits a number or operator
            ship_number_collisions = pygame.sprite.spritecollide(self.player_ship, self.present_numbers_operators, True)

            for element in self.present_numbers_operators:

                if ship_number_collisions:

                    element.reset()
                    element.toggle()
                    self.present_numbers_operators.empty()
                    del self.x_positions[:]

                elif element.YPosition() > 480:

                    element.reset()
                    self.present_numbers_operators.empty()
                    element.toggle()
                    self.player_ship.ReduceLives()

                    del self.x_positions[:]
                    
                else:

                    element.update()

                    if not self.stop_moving:

                        if count_choice == 11:
                            count_choice = 0
                            choice += 1

                            if choice == len(self.x_positions):
                                choice = 0

                            self.player_ship.update(self.x_positions[choice], 620)

            for element in ship_number_collisions:

                if not self.stop_moving:
                    self.player_ship.ReduceLives()
                    self.accumulating_answer = 0
                    self.hit_number = False
                    self.hit_operator = False
                    first_time = True

                elif self.stop_moving:

                    if (self.hit_number) and (self.hit_operator):
                        self.accumulating_answer = self.Operation(self.temporary_operator, self.accumulating_answer, element.getValue())
                        self.number_operators_used += 1
                        print self.accumulating_answer

                        self.hit_number = True
                        self.hit_operator = False
                        second_time = False

                    elif self.hit_operator:
                        self.temporary_operator = element.getOperator()
                        second_time = True
                        print element.getOperator()

                    elif self.hit_number and (first_time):
                        self.accumulating_answer = element.getValue()
                        first_time = False
                        print self.accumulating_answer

                self.stop_moving = False

                choice = 0
                count_choice = 0

                element.toggle()
                element.reset()

                self.present_numbers_operators.empty()
                del self.x_positions[:]
                pygame.time.delay(1000)

            # Moves on to the next number as an answer if the accumulating_answer equals to the given number.
            # Calculates points depending on how many operators are used.
            if self.accumulating_answer == self.answer_numbers[self.answer_numbers_index]:

                self.accumulating_answer = 0

                self.answer_numbers_index += 1

                self.hit_number = False
                self.hit_operator = False
                first_time = True
                self.stop_moving = False
                choice = 0
                count_choice = 0

                if (self.number_operators_used > 0) and (self.number_operators_used <= 2):
                    self.points += 100

                elif (self.number_operators_used > 2) and (self.number_operators_used <= 5):
                    self.points += 50

                else:
                    self.points += 25

            # Ends game when the player runs out of lives
            if self.player_ship.CurrentLives() == 0:
                break

            self.ships.draw(self.screen)
            self.present_numbers_operators.draw(self.screen)

            self.changeInfo()

            pygame.display.flip()

            self.screen.fill(self.background_color)

        self.endGame()

if __name__ == '__main__':

    GalagaVariant().Parameters()

