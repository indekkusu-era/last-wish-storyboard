from utils.sb import StoryBoard
from visualizer import Visualizer

audio_fp = "Kry.exe - Last Wish (feat. Ice).wav"

visualizer = Visualizer(audio_fp)

objects = visualizer.render(ms=33, max_length=0.6)

sb = StoryBoard(objects)
sb.osb('test.osb')
