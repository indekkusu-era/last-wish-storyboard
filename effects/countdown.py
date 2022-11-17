from utils.objects import Sprite
from utils.objects.actions import Move, Color, Scale, Fade, Loop
from utils.objects.images import get_text_image

def generate_number_sprites(font: str, size: int):
    for i in range(10):
        number = get_text_image(str(i), font, size)
        fp = f"sb/number_{i}.png"
        n_sprite = Sprite(fp)
        n_sprite.from_image(number)

class Countdown:
    def __init__(self, start, end):
        self._start = start
        self._end = end
    
    def _duration(self):
        """returns duration in seconds"""
        return (self._end - self._start) // 1000
    
    @staticmethod
    def render_numbers(num: int, time: int, pos: tuple):
        cur_num = [0 for _ in str(num)]
        offset_fadein = [time for _ in str(num)]
        t = time
        for n in range(num, -1, -1):
            # check if any number changes
            new_num = [int(i) for i in list(str(n))]
            while len(new_num) < len(str(num)):
                new_num = [0] + new_num
            for j, (cur, new) in enumerate(zip(cur_num, new_num)):
                if cur == new:
                    continue
                fp = f"sb/number_{cur}.png"
                num_sprite = Sprite(fp, align='CentreRight')
                num_sprite.add_action(Fade(0, offset_fadein[j] - 1, offset_fadein[j], 0, 1))
                num_sprite.add_action(Move(0, offset_fadein[j], t, (j * 30 + pos[0], pos[1]), (j * 30 + pos[0], pos[1])))
                num_sprite.add_action(Fade(0, t, t+1, 1, 0))
                offset_fadein[j] = t
                yield num_sprite
            cur_num = new_num
            t += 1000

    def render(self):
        dur = self._duration()
        return list(self.render_numbers(dur, self._start, (580, 120)))
