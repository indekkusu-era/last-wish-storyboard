'''
*    Title: Mapper's Parts for Storyboard
*    Author: Polytetral
*    Date: 17th November 2022
'''

from utils.objects import Fade, Move, MoveY, VectorScale, Color
from utils.sb import Sprite
from .countdown import Countdown
from utils.objects.images import get_text_image
from  .vocal_text import VocalText
from utils.constants.constants import mappers

#flashing color for bar 4 measures before the end of drain bar -> component 2 for end
#redtransitions = [Color(0, tstart, tend, (255, 255, 255), (255, 0, 0)), Color(0, tstart, tend, (255, 0, 0), (255, 255, 255))]
#redloop = Loop(tstart, 4, redtransitions)
#timebar.add_action(redloop)

#generator function takes in start time of bar, end time of bar, bpm, mapper, card name and creates sprites for these objects accordingly
class Part:
    def __init__(self, mapper_name, card_name, t_start, t_end):
        self.mapper_name = mapper_name
        self.card_name = card_name
        self.t_start = t_start
        self.t_end = t_end
            
    def mapper(self):
        #returns name of mapper given
        return self.mapper_name
    
    def cardname(self):
        #returns name of card given
        return self.card_name
    
    def starttime(self):
        #returns start of bar in milliseconds
        return self.t_start
    
    def endtime(self):
        #returns end of bar in milliseconds
        return self.t_end
    
    def countdown(self):
        return Countdown(self.t_start, self.t_end).render()
    
    def render(self):
        glitch_mapper_name = VocalText(self.mapper_name, 30, 'resources/source_serif.ttf', 5)
        glitch_spell_card = VocalText(self.card_name, 20, 'resources/source_serif.ttf', 5)
        mapper_name_sprites = glitch_mapper_name.render(self.t_start, self.t_start + 500, self.t_end, 20, (320, 50))
        card_sprites = glitch_spell_card.render(self.t_start, self.t_start + 500, self.t_end, 15, (320, 80))

        for i in range(5):
            mapper_name_sprites[i].add_action(Color(0, self.t_start, self.t_start + 500, (255, 0, 0), (255, 0, 0)))
            card_sprites[i].add_action(Color(0, self.t_start, self.t_start + 500, (255, 0, 0), (255, 0, 0)))

        mapper_name_sprites[-1].add_action(Color(0, self.t_start + 500, self.t_end, (255,0,0), (255,0,0)))
        card_sprites[-1].add_action(Color(0, self.t_start + 500, self.t_end, (255,0,0), (255,0,0)))
        
        all_sprites = []

        black = Sprite("sb/white.png")
        black.add_action(Color(0, self.t_start, self.t_end, (0,0,0), (0,0,0)))
        black.add_action(Fade(0, self.t_start, self.t_end, 0.75, 0.75))
        black.add_action(VectorScale(0, self.t_start, self.t_end, (1, 0.3), (1, 0.3)))
        black.add_action(MoveY(0, self.t_start, self.t_end, 0, 0))

        all_sprites.append(black)

        timebar = Sprite(f"sb/white.png", align = "CentreLeft")
        timebar.add_action(Fade(0, self.t_start, self.t_end, 0.75, 0.75))
        timebar.add_action(Move(0, self.t_start, self.t_end, (-150, 0), (-150, 0)))
        timebar.add_action(VectorScale(0, self.t_start, self.t_start + 500, (0, 0.3), (0.8, 0.3)))
        timebar.add_action(VectorScale(0, self.t_start, self.t_end, (0.8, 0.3), (0.0, 0.3)))

        all_sprites.append(timebar)

        all_sprites += mapper_name_sprites + card_sprites

        return all_sprites

#effect: generates bar on top with mapper name below, then their card name
#fades in from the left, fades out to the right
def mapper_bar(part: Part):
    name = part.mapper()
    card = part.cardname()
    start = part.starttime()
    end = part.endtime()
    
    all_sprites = []
    
    card_fname = card.replace("\n", "_").replace("_", " ").replace("\"", "")
    mappername = Sprite(f"sb/{name}.png", align="CentreLeft") #name of the mapper
    cardname = Sprite(f"sb/{card_fname}.png", align="CentreLeft") #name of the mapper card
    mappername.from_image(get_text_image(name, 'resources/source_serif.ttf', 30))
    cardname.from_image(get_text_image(card, 'resources/source_serif.ttf', 20))
    timebar = Sprite(f"sb/white.png", align = "CentreLeft") #this bar should span the length minus some border pixels

    timebar.add_action(VectorScale(0, start, end, (0.5, 0.025), (0.0, 0.025))) #(1.0, 1.0) start size, (0.0, 1.0) end size
    
    #fade+move in and outs for the names etc
    standardfadein = Fade(0, start, start+314, 0, 1)
    standardfadeout = Fade(0, end-314, end, 1, 0)
    
    #add for all fades
    mappername.add_action(standardfadein)
    mappername.add_action(standardfadeout)
    cardname.add_action(standardfadein)
    cardname.add_action(standardfadeout)
    timebar.add_action(standardfadein)
    timebar.add_action(standardfadeout)

    #add for all moves
    delay = 314
    timebar.add_action(Move(0, start, start+delay, (0, 70), (20, 70)))
    timebar.add_action(Move(0, end-delay, end, (20, 70), (40, 70)))
    mappername.add_action(Move(0, start, start+delay, (0, 120), (20, 120)))
    mappername.add_action(Move(0, end-delay, end, (20, 120), (40, 120)))
    cardname.add_action(Move(0, start, start+delay, (0, 160), (20, 160)))
    cardname.add_action(Move(0, end-delay, end, (20, 160), (40, 160)))
    
    all_sprites.extend([mappername, cardname])
    all_sprites += part.countdown()
    return all_sprites

def mapper_bar_2(part: Part):
    name = part.mapper()
    card = part.cardname()
    start = part.starttime()
    end = part.endtime()

    all_sprites = []
    
    # get mapper name and card name
    card_fname = card.replace("\n", "_").replace(" ", "_").replace("\"", "")
    mappername = Sprite(f"sb/{name}.png") #name of the mapper
    cardname = Sprite(f"sb/{card_fname}.png") #name of the mapper card
    mappername.from_image(get_text_image(name, 'resources/source_serif.ttf', 30))
    cardname.from_image(get_text_image(card, 'resources/source_serif.ttf', 20))
    black = Sprite("sb/white.png")
    timer_bar_left = Sprite("sb/white.png", align="CentreLeft") # timer bar
    timer_bar_right = Sprite("sb/white.png", align="CentreRight") # another timer bar

    delay = 1000
    
    black.add_action(Color(0, start-delay, end+delay, (0,0,0), (0,0,0)))
    black.add_action(Fade(0, start - delay, end + delay, 0.75, 0.75))
    black.add_action(VectorScale(0, start - delay, end + delay, (1, 0.3), (1, 0.3)))
    black.add_action(MoveY(0, start - delay, start, -120, 0))
    black.add_action(MoveY(0, end, end + delay, 0, -120))
    
    mappername.add_action(MoveY(0, start - delay, start, -70, 50))
    mappername.add_action(MoveY(0, end, end + delay, 50, -70))

    cardname.add_action(MoveY(0, start - delay, start, -40, 80))
    cardname.add_action(MoveY(0, end, end + delay, 80, -40))

    timer_bar_left.add_action(Fade(0, start - delay, end + delay, 0.75, 0.75))
    timer_bar_left.add_action(Move(0, start, end, (-150, 0), (-150, 0)))
    timer_bar_left.add_action(VectorScale(0, start - delay, start, (0.25, 0.3), (0.25, 0.3)))
    timer_bar_left.add_action(VectorScale(0, start, end + delay, (0.25, 0.3), (0, 0.3)))
    timer_bar_left.add_action(MoveY(0, start - delay, start, -120, 0))
    timer_bar_left.add_action(MoveY(0, end, end + delay, 0, -120))

    timer_bar_right.add_action(Fade(0, start - delay, end + delay, 0.75, 0.75))
    timer_bar_right.add_action(Move(0, start, end, (790, 0), (790, 0)))
    timer_bar_right.add_action(VectorScale(0, start - delay, start, (0.25, 0.3), (0.25, 0.3)))
    timer_bar_right.add_action(VectorScale(0, start, end + delay, (0.25, 0.3), (0, 0.3)))
    timer_bar_right.add_action(MoveY(0, start - delay, start, -120, 0))
    timer_bar_right.add_action(MoveY(0, end, end + delay, 0, -120))

    all_sprites += [black, mappername, cardname, timer_bar_left, timer_bar_right]

    return all_sprites

def mapper_bar_3(part: Part):
    return part.render()

def generate_parts(mappers, end):
    all_bars = []
    parts = list(mappers.keys()) + [end]
    intervals = list(zip(parts[:-1], parts[1:]))
    for (t0, t1), (name, spellcard) in zip(intervals, mappers.values()):
        part = Part(name, spellcard, t0, t1)
        all_bars.extend(part.render())
    return all_bars

def all_parts():
    return generate_parts(mappers, 330103)
