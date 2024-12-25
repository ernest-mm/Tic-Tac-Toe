# I'm creating this file because I wasn't able to load the paper sound inside the init methos of the game.
# I kept having a weird bug where pygame.mixer.Sound was not initializing.

import pygame

def load_sound(path: str) -> pygame.mixer.Sound: 
    """
    Return a pygame.mixer.Sound object if the loading for successful,
    None, with an error message printed in the other case.
    """
    pygame.mixer.init()

    try:
        paper_sound = pygame.mixer.Sound(path)
        return paper_sound
    except pygame.error as e:
        print(f"Failed to load sound: {e}")
        return None
    
def play_sound(sound: pygame.mixer.Sound) -> None:
    sound.play()