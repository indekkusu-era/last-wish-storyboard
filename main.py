import os
import numpy as np
from utils.sb import StoryBoard
from effects.visualizer import last_wish_visualizer
from effects.vocal_text import VocalText
from effects.darken import do_you_think_i_want_this, i_wont_leave_you_behind, this_is_your_last_wish, intro
from effects.mapper_transition import MapperTransition
from parts import MappersList, FadeInFadeOut, TransitionToMapper
from utils.constants.constants import mappers_list, SB_DEFAULT_X, SB_DEFAULT_Y
from utils.objects.images import get_text_image
from utils.objects import Rotate

np.random.seed(8)

audio_fp = "Kry.exe - Last Wish (feat. Ice).wav"
font = 'resources/NewRocker-Regular.ttf'

text_timestamps = {
    (41052, 42052, 42552): "Do you think I want this?",
    (191603, 192853, 193603): "I won't leave you behind.",
    (256503, 257103, 257503): "This is your last wish"
}

intro_text = {
    (2285,6857): "o!mLN3",
    (4571,6857): "Grand Finals Tiebreaker",
    (6857,11428): "Kry.exe",
    (9142,11428): "Last Wish (feat. Ice)"
}

def create_if_not_exist(dir):
    if os.path.isdir(dir):
        return
    os.mkdir(dir)

def create_folders():
    create_if_not_exist('sb')
    create_if_not_exist('sb/mappers')

def storyboard():
    background_objects = []
    foreground_objects = []
    overlay_objects = []

    # add visualizer into the background
    visualizer = last_wish_visualizer()
    background_objects += visualizer

    # dark objects
    darkened_objects = [do_you_think_i_want_this(), i_wont_leave_you_behind(), this_is_your_last_wish(), intro()]
    background_objects += darkened_objects

    # mapper transitions
    # sample_transition = MapperTransition('HowToPlayLN', 'Normal Distribution', 'sb/mappers/htpln.png')
    # background_objects += sample_transition.transition((157714, 158514), (159314, 160114), "resources/NewRocker-Regular.ttf", 30)

    # intro text
    for i, ((t_start, t_end), text) in enumerate(intro_text.items()):
        pos = (SB_DEFAULT_X // 2, SB_DEFAULT_Y // 4)
        if i % 2:
            pos = (SB_DEFAULT_X - pos[0], SB_DEFAULT_Y - pos[1])
        
        text_intro = FadeInFadeOut(text, font, 50)
        text_sprite = text_intro.render(pos, t_start, t_end)
        background_objects.append(text_sprite)
    
    # add transition to mappers
    _nine = get_text_image('9', font, 100)
    nine = TransitionToMapper('sb/nine.png').render(11428, 11714, 13714)
    nine.from_image(_nine)
    background_objects.append(nine)
    circle = TransitionToMapper('sb/Magic_Circle.png').render(11428, 11714, 13714, scale=0.15)
    circle.add_action(Rotate(0, 11428, 13714, 0, 1337/180*3.14))
    background_objects.append(circle)

    # add mappers list
    mapperslist = MappersList(mappers_list)
    appear_time = [12571, 12642, 12785, 12928, 13071, 13214, 13357, 13428, 13571]
    mapper_sprites = mapperslist.render(appear_time, 13714, font, 30)
    background_objects += mapper_sprites

    # add vocal text at foreground
    for timestamp, text in text_timestamps.items():
        sps = VocalText(text, 50, font, 5)
        foreground_objects += sps.render(*timestamp, period=25)

    sb = StoryBoard(background_objects, foreground_objects, overlay_objects)
    return sb

def main():
    create_folders()
    osb_fp = "Kry.exe - Last Wish (feat. Ice) (FelixSpade).osb"
    sb = storyboard()
    sb.osb(osb_fp)

if __name__ == "__main__":
    main()
