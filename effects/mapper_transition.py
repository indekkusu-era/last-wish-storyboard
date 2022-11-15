from PIL import Image
from utils.objects.sprite import Sprite
from utils.objects.actions import Move, Color, Scale
from utils.objects.images import get_text_image

class MapperTransition:
    def __init__(self, mapper_name: str, spellcard: str, mapper_pic_fp: str) -> None:
        self._name = mapper_name
        self._spell = spellcard
        self._profile_fp = mapper_pic_fp
        self._generate_sprite()

    def _generate_sprite(self):
        self._profile = Image.open(self._profile_fp)
        self._sprite = Sprite(self._profile_fp)
        self._sprite.from_image(self._profile)
    
    def transition(self, offset_in: tuple, offset_out: tuple, font_fp, size):
        # mapper name
        mapper_name = Sprite(f'sb/{self._name}.png')
        # spell card
        spell_card = Sprite(f'sb/{self._name}_card.png')
        # white background
        def white_bg():
            return Sprite('sb/white.png')
        
        mapper_name.from_image(get_text_image(self._name, font_fp, size))
        spell_card.from_image(get_text_image(self._spell, font_fp, size))

        in0, in1 = offset_in
        out0, out1 = offset_out

        # Add move in, move out to mapper name from the left
        mapper_name.add_action(Move(1, in0, in1, (-640, 160), (160, 160)))
        mapper_name.add_action(Move(2, out0, out1, (160, 160), (-640, 160)))

        # Add move in, move out to spell-card name from the right
        spell_card.add_action(Move(1, in0, in1, (1280, 320), (480, 320)))
        spell_card.add_action(Move(2, out0, out1, (480, 320), (1280, 320)))

        # Add move in and scale out for mapper profile pic
        self._sprite.add_action(Move(1, in0, in1, (320, 480), (320, 240)))
        self._sprite.add_action(Scale(2, out0, out1, 0.1, 0))

        return [mapper_name, spell_card]
