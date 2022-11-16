import numpy as np
from utils.objects.images import get_text_image, glitch_crop
from utils.objects.sprite import Sprite
from utils.objects.actions import Fade, Move
from utils.constants.constants import SB_DEFAULT_X, SB_DEFAULT_Y

class VocalText:
    def __init__(self, text: str, font_size: int, font_fp: str, n_glitch_portions: int):
        self._text = text
        self._font_size = font_size
        self._font_fp = font_fp
        self._n_portions = n_glitch_portions
        self._get_glitch()
        
    def _get_glitch(self):
        text_image = get_text_image(self._text, self._font_fp, self._font_size)
        self._glitched_image = list(glitch_crop(text_image, self._n_portions))
    
    def render(self, t0, t1, period=50):
        list_sprites = []
        t = t0
        opacity_slope = 1 / (t1 - t0)
        fp_name = self._text.replace(" ", "_").replace("?", "_").replace(".", "")
        for i in range(len(self._glitched_image)):
            sp = Sprite(f"sb/{fp_name}{i}.png")
            sp.from_image(self._glitched_image[i])
            sp.add_action(Move(0, t0 // 3 + t1 * 2 // 3 + 51, t0 // 3 + t1 * 2 // 3 + 52, (SB_DEFAULT_X // 2, SB_DEFAULT_Y // 2), (SB_DEFAULT_X // 2, SB_DEFAULT_Y // 2)))
            sp.add_action(Fade(0, t0 // 3 + t1 * 2 // 3 + 51, t0 // 3 + t1 * 2 // 3 + 52, 1, 1))
            sp.add_action(Fade(0, t1 - 1, t1, 1, 0))
            list_sprites.append(sp)

        while t <= t0 // 3 + t1 * 2 // 3:
            rng = np.sort(np.random.uniform(0, 1, (len(self._glitched_image),2)) * period, axis=1)
            for i in range(len(list_sprites)):
                start, end = rng[i]
                opacity = ((t + start) - t0) * opacity_slope
                offset = (2 * (i % 2) - 1) * (1 - (t1 - (t + start)) / (t1 - t0)) * 20 + SB_DEFAULT_X // 2
                list_sprites[i].add_action(Move(0, t + start - 1, t + start, (offset, SB_DEFAULT_Y // 2), (offset, SB_DEFAULT_Y // 2)))
                list_sprites[i].add_action(Fade(0, t + start - 1, t + start, 0, opacity))
                list_sprites[i].add_action(Fade(0, t + end - 1, t + end, opacity, 0))
            t += period
        
        return list_sprites
