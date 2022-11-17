'''
*    Title: Mapper's Parts for Storyboard
*    Author: Polytetral
*    Date: 17th November 2022
'''

from utils.objects import Fade, Move, VectorScale
from utils.sb import Sprite, StoryBoard

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
        #returns name of card given
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
    timebar = Sprite("timebar.png", align = "CentreLeft") #this bar should span the length minus some border pixels

    timebar.add_action(VectorScale(0, start, end, (1.0, 1.0), (0.0, 1.0))) #(1.0, 1.0) start size, (0.0, 1.0) end size
    
    #fade+move in and outs for the names etc
    standardfadein = Fade(0, start, start+314, 0, 100)
    standardfadeout = Fade(0, end-314, end, 100, 0)
    
    #add for all fades
    mappername.add_action(standardfadein)
    mappername.add_action(standardfadeout)
    cardname.add_action(standardfadein)
    cardname.add_action(standardfadeout)
    timebar.add_action(standardfadein)
    timebar.add_action(standardfadeout)

    #add for all moves
    timebar.add_action(Move(0, start, start+314, (0, 20), (20, 20)))
    timebar.add_action(Move(0, end-314, end, (20, 20), (40, 20)))
    mappername.add_action(Move(0, start, start+314, (0, 50), (20, 50)))
    mappername.add_action(Move(0, end-314, end, (20, 50), (40, 50)))
    cardname.add_action(Move(0, start, start+314, (0, 70), (20, 70)))
    cardname.add_action(Move(0, end-314, end, (20, 70), (40, 70)))
    
    all_sprites.extend([timebar, mappername, cardname])
    return all_sprites
    
def all_parts():
    #htpln = Part("HowToPlayLN", "LNCrypted Memories \"Corrupted Fragments\"", 2285, 13714) example， but is now omitted cus of intro
    #fill in spellcard names when mappers have input their card names
    funk1 = Part("TheFunk", "Phantom Hallucination \"Encryptic Storm\"", 13714, 32000)
    funk2 = Part("TheFunk", "Phantom Hallucination \"Apocalyptic Devination\"", 32000, 42552)
    sere1 = Part("[Crz]Crysarlene", "Serenity \"Calm Before The Apocalypse\"", 42552, 66552)
    sere2 = Part("[Crz]Crysarlene", "Serenity \"The Great Depression\"", 66552, 82552)
    #chxu1 = Part("chxu", "something", 82552, 98552)
    #logan = Part("Logan636", "something", 98552, 119322)
    mango1 = Part("doctormango", "Havoc \"Doppelganger Syndrome\"", 119322, 133037)
    felix1 = Part("FelixSpade", "Illusion Art \"Berserker's Haze\"", 133037, 159314)
    akats = Part("ERA Hatsuki", "The Great \"eLegaNtic Outburst\"", 159314, 191603)
    mango2 = Part("doctormango", "Havoc \"Suspense\"", 191603, 209603)
    #chxu2 = Part("chxu", "something1", 209603, 225603)
    #chxu3 = Part("chxu", "something2", 225603, 257603)
    hylotl1 = Part("Hylotl", "TBC", 257603, 273603)
    danny1 = Part("DannyPX", "TBC", 273603, 289603)
    felix2 = Part("FelixSpade", "Illusion Art \"Doomsday Reverie\"", 289603, 305603)
    hylotl2 = Part("Hylotl", "TBC", 305603, 321603)
    danny2 = Part("DannyPX", "TBC", 321603, 330103)
    
    #add all parts (im lazy to generalize since its a countable number lmao)
    all_bars = []
    all_bars.extend(mapper_bar(funk1))
    all_bars.extend(mapper_bar(funk2))
    all_bars.extend(mapper_bar(sere1))
    all_bars.extend(mapper_bar(sere2))
    #all_bars.extend(mapper_bar(chxu1))
    #all_bars.extend(mapper_bar(logan))
    all_bars.extend(mapper_bar(mango1))
    all_bars.extend(mapper_bar(felix1))
    all_bars.extend(mapper_bar(akats))
    all_bars.extend(mapper_bar(mango2))
    #all_bars.extend(mapper_bar(chxu2))
    #all_bars.extend(mapper_bar(chxu3))
    all_bars.extend(mapper_bar(hylotl1))
    all_bars.extend(mapper_bar(danny1))
    all_bars.extend(mapper_bar(felix2))
    all_bars.extend(mapper_bar(hylotl2))
    all_bars.extend(mapper_bar(danny2))
    
    bars_sb = StoryBoard(background_objects = all_bars)
    bars_sb.osb("drainbars.osb")
