from utils.sb import StoryBoard
from effects.visualizer import last_wish_visualizer

audio_fp = "Kry.exe - Last Wish (feat. Ice).wav"

def storyboard():
    background_objects = []
    foreground_objects = []
    overlay_objects = []

    # add visualizer into the background
    visualizer = last_wish_visualizer()
    background_objects += visualizer

    sb = StoryBoard(background_objects, foreground_objects, overlay_objects)
    return sb

def main():
    osb_fp = "Kry.exe - Last Wish (feat. Ice) (FelixSpade).osb"
    sb = storyboard()
    sb.osb(osb_fp)

if __name__ == "__main__":
    main()
