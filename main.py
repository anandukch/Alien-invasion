import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import function as fn

def game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('alien')
    ship=Ship(screen,ai_settings)
    bullets=Group()
    # alien=Alien(a1_settings,screen)
    aliens=Group()
    fn.create_fleet(ai_settings,screen,ship,aliens)
    while True:

        fn.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        fn.update_bullets(aliens,bullets)
        fn.update_aliens(ai_settings,aliens)
        fn.update_screen(ai_settings,screen,ship,aliens,bullets)


if __name__ == '__main__':
    game()






