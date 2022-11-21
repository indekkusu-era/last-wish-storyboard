from utils.objects import Sprite
from utils.objects import Move, Fade
from utils.objects.images import get_text_image

from utils.constants.constants import SB_DEFAULT_X, SB_DEFAULT_Y

class MappersList:
    def __init__(self, mappers_list: list):
        self._mappers_list = mappers_list
    
    def _render(self, appearance_time: list, end_time: int, font: str, size: int):
        assert len(self._mappers_list) == len(appearance_time)
        for i, (mapper, appear_time) in enumerate(zip(self._mappers_list, appearance_time)):
            mapper_sprite = Sprite(f'sb/{mapper}.png')
            mapper_sprite.from_image(get_text_image(mapper, font, size))
            scroll_time = appearance_time[(i + 1)::2]
            scroll_up = 2 * (i % 2) - 1
            initial_actions = [
                Move(0, appear_time, appear_time, (SB_DEFAULT_X // 2, SB_DEFAULT_Y // 2), (SB_DEFAULT_X // 2, SB_DEFAULT_Y // 2)), 
                Fade(0, appear_time - 1, appear_time, 0, 1), Fade(0, end_time, end_time + 3000, 1, 0)
            ]
            mapper_sprite.add_actions(initial_actions)
            next_pos = SB_DEFAULT_Y // 2
            for t in scroll_time:
                next_pos += scroll_up * (SB_DEFAULT_Y // 3) / len(self._mappers_list) * 2
                mapper_sprite.add_action(Move(0, t - 1, t, (SB_DEFAULT_X // 2, next_pos), (SB_DEFAULT_X // 2, next_pos)))
            yield mapper_sprite
        
    def render(self, appearance_time: list, end_time: int, font: str, size: int):
        return list(self._render(appearance_time, end_time, font, size))
