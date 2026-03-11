from Soundtracks import *
from SoundPrompt import *
from Options import *
from Menues import *
from Intro import *
from Credits import *

coming_soon = lambda: print(system.communicate("Coming soon...", "LIGHTWHITE_EX"))

# SOUNDTRACKS
jazz1_option = Option("Jazz1", jazz1)
jazz2_option = Option("Jazz2", jazz2)
jazz3_option = Option("Jazz3", jazz3)
turn_off_soundtrack_option = Option("Turn Off", Soundtrack.turn_off_soundtrack)
from_soundtracks_to_audio = Option("Back - Audio", system.communicate)

soundtracks_options = (jazz1_option, jazz2_option, jazz3_option, turn_off_soundtrack_option, from_soundtracks_to_audio)
soundtracks_menu = MenuPattern("Soundtracks", soundtracks_options)

# SOUNDS
toggle_sound_option = Option("Turn Off/On", sound_prompt)
from_sounds_to_audio = Option("Back - Audio", system.communicate)

sounds_options = (toggle_sound_option, from_sounds_to_audio)
sounds_menu = MenuPattern("Sounds", sounds_options)

# AUDIO
soundtracks_option = Option("Soundtracks", soundtracks_menu)
sounds_option = Option("Sounds", sounds_menu)
from_audio_to_settings = Option("Back - Settings", system.communicate)

audio_options = (soundtracks_option, sounds_option, from_audio_to_settings)
audio_menu = MenuPattern("Audio", audio_options)

# SETTINGS
rules_option = Option("Rules", system.get_rules)
audio_option = Option("Audio", audio_menu)
credits_option = Option("Credits", credits_menu)
from_settings_to_main_menu = Option("Back - Main Menu", system.communicate)

settings_options = (rules_option, audio_option, credits_option, from_settings_to_main_menu)
settings_menu = MenuPattern("Settings", settings_options)

# MAIN MENU
play_option = Option("Play", coming_soon)
settings_option = Option("Settings", settings_menu)
quit_option = Option("Quit", system.quit_game)

main_menu_options = (play_option, settings_option, quit_option)
main_menu = MenuPattern("Main Menu", main_menu_options)


def game():
    game_intro()
    main_menu()


game()
