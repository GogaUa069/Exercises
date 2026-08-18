from data_saver import *


def soundtrack(name, loops=1):
    path = f"../AUDIO/SOUNDTRACKS/{name}"
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(loops=loops)


def sound(name, loops=1, maxtime=0, fade_ms=0):
    path = data_saver_txt.resource_path(f"../AUDIO/SOUNDS/{name}")
    s = pygame.mixer.Sound(path)
    maxtime = maxtime if maxtime else int(s.get_length() * 1000)
    s.play(loops=loops, maxtime=maxtime, fade_ms=fade_ms)
