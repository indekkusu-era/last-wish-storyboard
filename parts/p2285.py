from utils.objects import Sprite
from utils.objects import Move, Fade, Scale
from utils.objects.images import get_text_image

from utils.constants.constants import SB_DEFAULT_X, SB_DEFAULT_Y

class FadeInFadeOut:
    def __init__(self, text: str, font: str, size: int):
        self._text = text
        self._font = font
        self._size = size
        self._sprite()
    
    def _sprite(self):
        fname = self._text.replace(" ", "_").replace("!", "")
        self.sprite = Sprite(f"sb/{fname}.png")
        self.sprite.from_image(get_text_image(self._text, self._font, self._size))
    
    def render(self, pos: tuple, t_start: int, t_end: int):
        fadein = Fade(0, t_start, t_start + 300, 0, 1)
        movein = Move(0, t_start, t_start + 300, (pos[0] - 50, pos[1]), pos)
        fadeout = Fade(2, t_end, t_end + 300, 1, 0)
        moveout = Move(2, t_end, t_end + 300, pos, (pos[0] + 50, pos[1]))

        self.sprite.add_actions([fadein, movein, fadeout, moveout])
        return self.sprite

class TransitionToMapper:
    def __init__(self, png):
        self._png = png
        self._get_sprite()
    
    def _get_sprite(self):
        self._sprite = Sprite(self._png)
    
    def render(self, t_start, t_stationary, t_end, scale=1):
        zoom1 = Scale(1, t_start, t_stationary, 10, scale)
        zoom2 = Scale(2, t_end, t_end + 500, scale, 0)
        opacity = Fade(0, t_start, t_end, 0.4, 0.4)
        self._sprite.add_actions([zoom1, zoom2, opacity])
        return self._sprite
