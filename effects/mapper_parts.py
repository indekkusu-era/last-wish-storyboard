'''
*    Title: Mapper's Parts for a Storyboard
*    Author: Polytetral
*    Date: 15th November 2022
'''

from utils.objects import Fade, Move, VectorScale
from utils.sb import Sprite

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
            
    @staticmethod
    def mapper(self):
        #returns name of mapper given
        return self.mapper_name
    
    @staticmethod
    def cardname(self):
        #returns name of care given
        return self.card_name
    
    @staticmethod
    def starttime(self):
        #returns start of bar in milliseconds
        return self.t_start
    
    @staticmethod
    def endtime(self):
        #returns end of bar in milliseconds
        return self.t_end

#effect: generates bar on top with mapper name below, then their card name
#fades in from the left, fades out to the right
def mapper_bar(part: Part):
    name = part.mapper()
    card = part.cardname()
    start = part.starttime()
    end = part.endtime()
    
    all_sprites = []
    
    mappername = Sprite("mappername.png") #name of the mapper
    cardname = Sprite("card.png") #name of the mapper card
    timebar = Sprite("timebar.png") #this bar should span the length minus some border pixels

    timebar.add_action(VectorScale(0, start, end, (1.0, 1.0), (0.0, 1.0))) #(1.0, 1.0) start size, (0.0, 1.0) end size
    
    #fade+move in and outs for the names etc
    standardfadein = Fade(0, start, start+10, 0, 100)
    standardfadeout = Fade(0, end-10, end, 100, 0)
    
    #add for all fades
    mappername.add_action(standardfadein)
    mappername.add_action(standardfadeout)
    cardname.add_action(standardfadein)
    cardname.add_action(standardfadeout)
    timebar.add_action(standardfadein)
    timebar.add_action(standardfadeout)

    #add for all moves
    timebar.add_action(Move(0, start, start+10, (0, 20), (20, 20)))
    timebar.add_action(Move(0, end-10, end, (20, 20), (40, 20)))
    mappername.add_action(Move(0, start, start+10, (0, 50), (20, 50)))
    mappername.add_action(Move(0, end-10, end, (20, 50), (40, 50)))
    cardname.add_action(Move(0, start, start+10, (0, 70), (20, 70)))
    cardname.add_action(Move(0, end-10, end, (20, 70), (40, 70)))
    
    all_sprites.extend([timebar, mappername, cardname])
    return all_sprites
    
#use case: take your case for example but idk if it works
def example_bar():
    htpln = Part("HowToPlayLN", "LNCrypted Memories \"Corrupted Fragments\"", 2285, 13714)
    part_sprites = mapper_bar(htpln)
    return part_sprites

