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
    
    def render(self, t0, t_stationary, t1, period=50, pos=(SB_DEFAULT_X // 2, SB_DEFAULT_Y // 2)):
        list_sprites = []
        t = t0
        opacity_slope = 1 / (t_stationary - t0)
        fp_name = self._text.replace(" ", "_").replace("?", "_").replace(".", "").replace("\"", "")
        text_image = get_text_image(self._text, self._font_fp, self._font_size)
        for i in range(len(self._glitched_image)):
            sp = Sprite(f"sb/{fp_name}{i}.png")
            sp.from_image(self._glitched_image[i])
            list_sprites.append(sp)
        
        full_sprite = Sprite(f"sb/{fp_name}_full.png")
        full_sprite.from_image(text_image)
        full_sprite.add_action(Move(0, t_stationary + period + 1, t_stationary + period + 2, pos, pos))
        full_sprite.add_action(Fade(0, t_stationary + period + 1, t_stationary + period + 2, 1, 1))
        full_sprite.add_action(Fade(0, t1 - 1, t1, 1, 0))

        while t < t_stationary:
            rng = np.sort(np.random.uniform(0, 1, (len(self._glitched_image),2)) * period, axis=1)
            for i in range(len(list_sprites)):
                start, end = rng[i]
                opacity = ((t + start) - t0) * opacity_slope
                offset = (2 * (i % 2) - 1) * (1 - (t_stationary - (t_stationary + start)) / (t_stationary - t0)) * 20 + pos[0]
                list_sprites[i].add_action(Move(0, t + start - 1, t + start, (offset, pos[1]), (offset, pos[1])))
                list_sprites[i].add_action(Fade(0, t + start - 1, t + start, 0, opacity))
                list_sprites[i].add_action(Fade(0, t + end - 1, t + end, opacity, 0))
            t += period
        
        return list_sprites + [full_sprite]
