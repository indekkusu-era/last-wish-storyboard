from utils.objects import *
from utils.objects.actions import Fade
from utils.constants.constants import SB_DEFAULT_X, SB_DEFAULT_Y

class CreditsText:
    def __init__(self, font_size: int, font_fp: str, slide: int, logo: bool):
        self._text = ""
        self._font_size = font_size
        self._font_fp = font_fp
        self._slide = slide
        self._logo = logo #whether there is a logo or not
        
    def insert_text(self, new_text):
        self._text += new_text
    
    def render(self, tstart, tend):
        all_sprites = []
        logo_sprites = []
        text_image = get_text_image(self._text, self._font_fp, self._font_size)
        credit_sprite = Sprite(f"sb/slide_{self._slide}.png") #image will be saved in the form "slide_1.png"
        credit_sprite.from_image(text_image)
        
        #text moves instantaneously to center, fades in slowly
        delay = 314
        logo_offset = 50 if self._logo else 0
        
        if self._logo:
            #add a bit more space on the top
            #i assume about 100 pixels is fine but ye reposition if needed
            logo_sprite = Sprite("sb/logo.png") #use logo
            logo_sprite.add_action(MoveY(0, tstart, tstart, 100, 100)) #idk move it to centre
            logo_sprite.add_action(Scale(0, tstart, tstart, 0.6, 0.6))
            logo_sprite.add_action(Fade(0, tstart, tstart + delay, 0.0, 1.0))
            logo_sprite.add_action(Fade(0, tend - delay, tend, 1.0, 0.0))

        credit_sprite.add_action(MoveY(0, tstart, tstart, SB_DEFAULT_Y/2 + logo_offset, SB_DEFAULT_Y/2 + logo_offset)) #idk move it to centre
        credit_sprite.add_action(Fade(0, tstart, tstart + delay, 0.0, 1.0))
        credit_sprite.add_action(Fade(0, tend - delay, tend, 1.0, 0.0))
        
        all_sprites.append(credit_sprite)
        if self._logo:
            all_sprites.append(logo_sprite)
        
        return all_sprites
    
def credits_roll():
    #example usage
    credit_slides = []
    slide1 = CreditsText(20, "resources/source_serif_bold.ttf", 1, False)
    slide2 = CreditsText(20, "resources/source_serif_bold.ttf", 2, True)
    
    with open('credits_text/slide1.txt', 'r') as f:
        slide1_text = f.read()
    
    with open('credits_text/slide2.txt', 'r') as f:
        slide2_text = f.read()

    slide1.insert_text(slide1_text)
    slide2.insert_text(slide2_text)
    
    credit_slides.extend(slide1.render(330103, 335103))
    credit_slides.extend(slide2.render(335103, 345103))
    
    return credit_slides
    
        
        
        