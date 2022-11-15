from utils.objects import Sprite
from utils.objects.actions import Color, Scale, Fade

def do_you_think_i_want_this():
    start, end = 40552, 42552
    sprite = Sprite('sb/white.png')
    sprite.add_action(Color(0, start, end, (0,0,0), (0,0,0)))
    sprite.add_action(Scale(0, start, end, 5, 5))
    return sprite

def i_wont_leave_you_behind():
    start, end = 189714, 191603
    start2, end2 = 193603, 209603
    sprite = Sprite('sb/white.png')
    sprite.add_action(Color(0, start, end2, (0,0,0), (0,0,0)))
    sprite.add_action(Scale(0, start, end2, 5, 5))
    sprite.add_action(Fade(0, start, end, 0, 1))
    sprite.add_action(Fade(0, start2, end2, 1, 0))
    return sprite

def this_is_your_last_wish():
    start, max_opa = 255603, 256603
    end = 257603
    sprite = Sprite('sb/white.png')
    sprite.add_action(Color(0, start, end, (0,0,0), (0,0,0)))
    sprite.add_action(Scale(0, start, end, 5, 5))
    sprite.add_action(Fade(0, start, max_opa, 0, 1))
    sprite.add_action(Fade(0, end, end + 1, 1, 0))
    return sprite
    