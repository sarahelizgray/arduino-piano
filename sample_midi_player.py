# play .mid music files using PyGame on your computer's sound card
# PyGame is free from: http://www.pygame.org/news.html
# tested with Python25 and PyGame171      vegaseat     27aug2007
import pygame

# pick a midi music file you have ...
# (if not in working folder use full path)
MUSIC_FILE = "daft_punk_da_funk.mid"

FREQ = 44100  # audio CD quality
BITSIZE= -16 # unsigned 16 bit
CHANNELS = 2    # 1 is mono, 2 is stereo
BUFFER = 1024    # number of samples
pygame.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)

# optional volume 0 to 1.0
pygame.mixer.music.set_volume(1.0)

def play_music(music_file):
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
        print "Music file %s loaded!" % music_file
    except pygame.error:
        print "File %s not found! (%s)" % (music_file, pygame.get_error())
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)

try:
    play_music(MUSIC_FILE)
except KeyboardInterrupt:
    # if user hits Ctrl/C then exit
    # (works only in console mode)
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.stop()
    raise SystemExit