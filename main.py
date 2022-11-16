import os
import numpy as np
from utils.sb import StoryBoard
from effects.visualizer import last_wish_visualizer
from effects.vocal_text import VocalText
from effects.darken import do_you_think_i_want_this, i_wont_leave_you_behind, this_is_your_last_wish
from effects.mapper_transition import MapperTransition
from parts import MappersList
from utils.constants.constants import mappers_list

np.random.seed(8)

audio_fp = "Kry.exe - Last Wish (feat. Ice).wav"

text_timestamps = {
    (41552, 42552): "Do you think I want this?",
    (191603, 193603): "I won't leave you behind.",
    (256503, 257503): "This is your last wish"
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
    darkened_objects = [do_you_think_i_want_this(), i_wont_leave_you_behind(), this_is_your_last_wish()]
    background_objects += darkened_objects

    # mapper transitions
    sample_transition = MapperTransition('HowToPlayLN', 'Normal Distribution', 'sb/mappers/htpln.png')
    background_objects += sample_transition.transition((157714, 158514), (159314, 160114), "resources/NewRocker-Regular.ttf", 30)

    # add mappers list
    mapperslist = MappersList(mappers_list)
    appear_time = [12571, 12642, 12785, 12928, 13071, 13214, 13357, 13428, 13571]
    mapper_sprites = mapperslist.render(appear_time, 13714, 'resources/NewRocker-Regular.ttf', 30)
    background_objects += mapper_sprites

    # add vocal text at foreground
    for timestamp, text in text_timestamps.items():
        sps = VocalText(text, 50, "resources/NewRocker-Regular.ttf", 5)
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
