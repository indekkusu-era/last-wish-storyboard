from utils.objects.images import get_text_image

im = get_text_image("Hello\nWorld\n\nIt's me", "resources/NewRocker-Regular.ttf", 50)

im.save('test.png')